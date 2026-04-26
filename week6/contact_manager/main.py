from fastapi import FastAPI
from pydantic import BaseModel
from pwdlib import PasswordHash
import jwt
from datetime import timedelta, datetime, timezone

SECRET_KEY = '1d8a683f6b2924fef1839ec2c66d59d6814e9c3325ec552953d144846c607414'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = PasswordHash.recommended()
DUMMY_HASH = pwd_context.hash('DUMMY PASSWORD')

app = FastAPI()

users = {
    'osamu_1':{
        'username': 'osamu_1',
        'email': 'osamu_1@gmail.com',
        'hashed_password': '83h$6jsdsdu^,;.dskaojedjdr#d%'
    }
}

class User(BaseModel):
    username: str
    email: str

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
        verify_password(password, DUMMY_HASH)
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
    
    
