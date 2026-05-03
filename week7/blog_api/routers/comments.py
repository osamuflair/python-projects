from fastapi import APIRouter, Depends
from typing import Annotated
from routers.users import UserInDb, get_current_user
from models import Comment
from datetime import datetime, timedelta, timezone

router = APIRouter(
    prefix = "/comment",
    tags = ["comments"]
)

comments = {}

@router.post("/")
def create_comment(current_user: Annotated[UserInDb, Depends(get_current_user)], comment: Comment):
    """a function that creates a comment"""
    comment = comment.model_dump()#converts the class to a dictionary
    WAT = timezone(timedelta(hours=1))  # West Africa Time
    timestamp = datetime.now(WAT)#stores the time the post is created
    author = current_user.user_name#stores the author of the comment
    if not comments:
        id = 1
    else:
        last_id = next(reversed(comments))#gives the value of the last key
        id = last_id + 1
        
    comment.update({"author": author, "timestamps": timestamp, "id": id})
    comments.update({id:comment})
    return ({"message": "sucessfully commented"})