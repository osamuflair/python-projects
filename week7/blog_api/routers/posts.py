from fastapi import APIRouter, Depends, HTTPException
from routers.users import get_current_user
from models import UserInDb, Post
from typing import Annotated
from datetime import datetime, timezone


router = APIRouter(
    prefix = "/posts",
    tags = ["post"]
)

posts = {}#uses a dictionary as the database

@router.post("/")
def create_post(current_user: Annotated[UserInDb, Depends(get_current_user)], post: Post):
    """a function that creates a post"""
    if current_user.role.lower() == "admin" or current_user.role.lower() == "author":
        post = post.model_dump()#converts the class to a dictionary
        timestamp = datetime.now(timezone.utc)#stores the time the post is created
        if not posts:
            id = 1
        else:
            last_id = next(reversed(posts))#gives the value of the last key
            id = last_id + 1
        
        post.update({"author": current_user.user_name, "timestamps": timestamp, "id": id})
        posts.update({id:post})
        return ({"message": "sucessfully created your post"})
    else:
        raise HTTPException(status_code = 403, detail = "UNAUTHORIZED")