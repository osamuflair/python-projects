from fastapi import FastAPI
from pydantic import BaseModel

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

