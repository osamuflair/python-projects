from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    user_name: str
    email: str
    role: str

class UserInDb(User):
    hashed_password: str

class Post(BaseModel):
    title: str
    content: str

class PostInDb(Post):
    timestamps: datetime
    id: int
    author: str

class Comment(BaseModel):
    content: str
    author: str
    post_id: int

class UserRegister(BaseModel):
    user_name: str
    email: str
    password: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str