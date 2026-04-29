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
    author: str

class PostInDb(Post):
    timestamps: datetime
    id: int

class Comment(BaseModel):
    content: str
    author: str
    post_id: int