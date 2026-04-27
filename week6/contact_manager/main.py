from fastapi import FastAPI
from pydantic import BaseModel
from pwdlib import PasswordHash
import jwt
from datetime import timedelta, datetime, timezone
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated

SECRET_KEY = '1d8a683f6b2924fef1839ec2c66d59d6814e9c3325ec552953d144846c607414'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = PasswordHash.recommended()
DUMMY_HASH = pwd_context.hash('DUMMY PASSWORD')#hashes a dummy password

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users = {
    'osamu_1':{
        'username': 'osamu_1',
        'email': 'osamu_1@gmail.com',
        'hashed_password': '$argon2id$v=19$m=65536,t=3,p=4$kD3+CW5BXK00W/sqyNdiTg$/C8xv+TbNAzEbFpGglUVeg8vKrnbvQs+NNZMjcBw97A'
    }
}

class User(BaseModel):
    username: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserInDb(User):
    hashed_password: str

def hash_password(password):
    """hashes a password"""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """checks if a password is same with the hashed password in database"""
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username):
    """checks if user is in database"""
    if username in users:
        user_dict = users[username]
        return UserInDb(**user_dict)
    
def authenticate_user(username, password):
    """checks if a user exists and if the password is correct"""
    user = get_user(username)
    if not user:
        verify_password(password, DUMMY_HASH)#verify over a dummy password to prevent timing attacks
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """encodes the data"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    jwt_encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_encoded
    
    
@app.post('/token')
def log_in(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    """its called when ever a user logs in"""
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub': user.username}, expires_delta=expires_delta)

    return Token(access_token=access_token, token_type='bearer')

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """It decodes the token to check if its valid, and has a valid user when ever a request is made"""
    error = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
            )
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = decoded.get('sub')
        if not username:
            raise error
        return get_user(username)
    except jwt.PyJWTError:
        raise error

@app.get('/users/me')
def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
