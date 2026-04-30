from fastapi import APIRouter
from pwdlib import PasswordHash
from models import UserRegister

router = APIRouter(
    prefix = "/users",
    tags = ["user"],
)

users = {}

passwordhash = PasswordHash.recommended()
DUMMYHASH = passwordhash.hash("DUMMYPASSWORD")


@router.post("/register/")
def user_registration(registration: UserRegister):
    registration = registration.model_dump()
    hashed_password = passwordhash.hash(registration["password"])
    del registration["password"]
    user_name = registration["user_name"]
    registration.update({"hashed_password": hashed_password})
    users.update({user_name: registration})

    return({"Message": "Successfully Registered"})
