from fastapi import APIRouter, Depends, HTTPException
from routers.users import get_current_user
from models import UserInDb, Post, PostInDb
from typing import Annotated
from datetime import datetime, timezone, timedelta
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
    prefix = "/posts",
    tags = ["post"]
)

posts = {}#uses a dictionary as the database

try:
    @router.post("/")
    def create_post(current_user: Annotated[UserInDb, Depends(get_current_user)], post: Post):
        """a function that creates a post"""
        if current_user.role.lower() == "admin" or current_user.role.lower() == "author":
            post = post.model_dump()#converts the class to a dictionary
            WAT = timezone(timedelta(hours=1))  # West Africa Time
            timestamp = datetime.now(WAT)#stores the time the post is created
            if not posts:
                id = 1
            else:
                last_id = next(reversed(posts))#gives the value of the last key
                id = last_id + 1
            
            post.update({"author": current_user.user_name, "timestamps": timestamp, "id": id})
            posts.update({id:post})
            logger.info("User successfully created a post")
            return ({"message": "sucessfully created your post"})
        else:
            logger.warning("Post creation failed - user is not authorized")
            raise HTTPException(status_code = 403, detail = "Only authors and admins can create posts")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise HTTPException(status_code=500, detail="Internal server error")

try:
    @router.put("/edit/{id}")
    def edit_posts(current_user: Annotated[UserInDb, Depends(get_current_user)], post: Post, id: int):
        """a function that edits an existing post"""
        if id in posts.keys():#checks if the post exists
            if (current_user.role.lower() == "author" and current_user.user_name == posts[id]["author"]) or current_user.role.lower() == "admin":
                #checks if the user is an author and if he owns the post or if the user is an admin
                posts[id]["title"] = post.title
                posts[id]["content"] = post.content
                #edits the post
                logger.info("User successfully edited a post")
                return ({"message": "Successfully edited post"})
            logger.warning("Post edit failed - user is not authorized")
            if current_user.role.lower() == "author":
                raise HTTPException(status_code = 403, detail = "Only authors that created a post can edit it")
            raise HTTPException(status_code = 403, detail = "Only authors and admins can edit posts")
        logger.warning("Post edit failed - post does not exist")
        raise HTTPException(status_code = 404, detail = "POST NOT FOUND")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise HTTPException(status_code=500, detail="Internal server error")

try:
    @router.delete("/delete/{id}")
    def delete_posts(current_user: Annotated[UserInDb, Depends(get_current_user)], id: int):
        """a function that deletes an existing post"""
        if id in posts.keys():#checks if the post exists
            if (current_user.role.lower() == "author" and current_user.user_name == posts[id]["author"]) or current_user.role.lower() == "admin":
                #checks if the user is an author and if he owns the post or if the user is an admin
                del posts[id]#deletes post
                logger.info("User successfully deleted a post")
                return({"message": "Successfully deleted post"})
            logger.warning("Post deletion failed - user is not authorized")
            if current_user.role.lower() == "author":
                raise HTTPException(status_code = 403, detail = "Only authors that created a post can delete it")
            raise HTTPException(status_code = 403, detail = "Only authors and admins can delete posts")
        logger.warning("Post deletion failed - post does not exists")
        raise HTTPException(status_code = 404, detail = "POST NOT FOUND")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise HTTPException(status_code=500, detail="Internal server error")

try:
    @router.get("/")
    def get_all_posts(current_user: Annotated[UserInDb, Depends(get_current_user)], page: int = 1, limit: int = 10):
        """returns all the posts"""
        skip = (page - 1) * limit
        logger.info("User successfully accessed all posts")
        return list(posts.values())[skip: skip + limit]#paginating the posts
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise HTTPException(status_code=500, detail="Internal server error")

try:
    @router.get("/{id}")
    def get_post(current_user: Annotated[UserInDb, Depends(get_current_user)], id: int):
        """returns a particular post"""
        if id in posts.keys():#checks if the post exists
            logger.info("User successfully accessed a post by id")
            return posts[id]
        logger.warning("Post access failed - post does not exists")
        raise HTTPException(status_code = 404, detail = "POST NOT FOUND")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise HTTPException(status_code=500, detail="Internal server error")