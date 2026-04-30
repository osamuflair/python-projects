from fastapi import APIRouter, Depends, HTTPException
from pwdlib import PasswordHash
from models import UserRegister, UserInDb, Token
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
import jwt
from datetime import datetime, timedelta, timezone

router = APIRouter(
    prefix = "/users",
    tags = ["user"],
)

router2 = APIRouter()

users = {}

passwordhash = PasswordHash.recommended()
DUMMYHASH = passwordhash.hash("DUMMYPASSWORD")

SECRET_KEY = '3aafc92f23d1774d08f727e242d5504c1f44753c08278cd0f78b9ba2a42399eb'
ALGORITHM = 'HS256'
DEFAULT_EXPIRY_MINUTE = 30

def hash_password(password):
    return passwordhash.hash(password)

@router.post("/register/")
def user_registration(registration: UserRegister):
    registration = registration.model_dump()
    hashed_password = hash_password(registration["password"])
    del registration["password"]
    user_name = registration["user_name"]
    registration.update({"hashed_password": hashed_password})
    users.update({user_name: registration})
    return({"Message": "Successfully Registered"})

def get_user(user_name):
    if user_name in users:
        user_dict = users[user_name]
        return UserInDb(**user_dict)
    
def verify_password(password, hashed_password):
    return passwordhash.verify(password, hashed_password)

def authenticate_user(user_name, password):
    user = get_user(user_name)
    if not user:
        verify_password(password, DUMMYHASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_token(data: dict, expire_delta: timedelta | None = None):
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
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
        status_code = 401,
        detail = "USER NOT FOUND"
        )
    expire_delta = timedelta(minutes = DEFAULT_EXPIRY_MINUTE)
    access_token = create_token(data = {"sub":user.user_name}, expire_delta = expire_delta)
    return Token(access_token = access_token, token_type = "bearer")

