from fastapi import APIRouter, Depends, HTTPException
from pwdlib import PasswordHash
from models import UserRegister, UserInDb, Token, User
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta, timezone

router = APIRouter(
    prefix = "/users",
    tags = ["user"],
)

router2 = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/token")

users = {}#uses a dictionary as the database

passwordhash = PasswordHash.recommended()
DUMMYHASH = passwordhash.hash("DUMMYPASSWORD")#hashed a dummy password

SECRET_KEY = '3aafc92f23d1774d08f727e242d5504c1f44753c08278cd0f78b9ba2a42399eb'
ALGORITHM = 'HS256'
DEFAULT_EXPIRY_MINUTE = 30

def hash_password(password):
    """"a function that hashes a password"""
    return passwordhash.hash(password)

@router.post("/register/")
def user_registration(registration: UserRegister):
    """
    a function that registers new users
    it hashes the user password, and gets rid of the plain password
    """
    registration = registration.model_dump()#converts the class to a dictionary
    hashed_password = hash_password(registration["password"])
    del registration["password"]
    user_name = registration["user_name"]
    registration.update({"hashed_password": hashed_password})
    users.update({user_name: registration})
    return({"Message": "Successfully Registered"})

def get_user(user_name):
    """
    it checks if user is in database
    and returns the user details 
    """
    if user_name in users:
        user_dict = users[user_name]
        return UserInDb(**user_dict)
    
def verify_password(password, hashed_password):
    """check if the provided password is the same with the one hashed"""
    return passwordhash.verify(password, hashed_password)

def authenticate_user(user_name, password):
    """it verify if the user exists
      and checks if the right password was inserted
      """
    user = get_user(user_name)
    if not user:
        verify_password(password, DUMMYHASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_token(data: dict, expire_delta: timedelta | None = None):
    """a function that encodes data using a secret key"""
    to_encode = data.copy()
    if not expire_delta:
        expiry_date = datetime.now(timezone.utc) + timedelta(minutes = 15)
    else:
        expiry_date = datetime.now(timezone.utc) + expire_delta
    to_encode.update({"exp": expiry_date})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded

@router2.post("/token")
def log_in(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    """it authenticate the user, encodes the user data and returns it as a token"""
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
        status_code = 401,
        detail = "Incorrect username or password"
        )
    expire_delta = timedelta(minutes = DEFAULT_EXPIRY_MINUTE)
    access_token = create_token(data = {"sub":user.user_name}, expire_delta = expire_delta)
    return Token(access_token = access_token, token_type = "bearer")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """a function that decodes tokens, and validates the decoded content"""
    error = HTTPException(
        status_code = 401,
        detail = "Could not validate credentials"
    )
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = decoded.get("sub")
        if not username:
            raise error
        return get_user(username)
    except jwt.PyJWTError:
        raise error
    
@router.get("/me")
def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    """
    a function that returns the current user
    it converts the class to a dictionary using .model_dump()
    it removes the hashed password by typecasting using model_validate
    """
    return User.model_validate(current_user.model_dump())