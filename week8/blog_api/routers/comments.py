from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from routers.users import UserInDb, get_current_user
from routers.posts import posts
from models import Comment
from datetime import datetime, timedelta, timezone
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix = "/comment",
    tags = ["comments"]
)

comments = {}

try:
    @router.post("/")
    def create_comment(current_user: Annotated[UserInDb, Depends(get_current_user)], comment: Comment):
        """a function that creates a comment"""
        if comment.post_id in posts:
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
            logger.info("User successfully commented on a post")
            return ({"message": "sucessfully commented"})
        logger.warning("Comment failed - post does not exists")
        raise HTTPException(status_code = 404, detail = "POST NOT FOUND")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise HTTPException(status_code=500, detail="Internal server error")

try:
    @router.get("/{post_id}/")
    def get_all_posts(current_user: Annotated[UserInDb, Depends(get_current_user)], post_id: int):
        """returns all comments from a particular post"""
        com = []
        for items in comments.values():
            if items["post_id"] == post_id:
                com.append(items)
        logger.info("User successfully accessed all comments")
        return list(com)
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise HTTPException(status_code=500, detail="Internal server error")