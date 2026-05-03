from fastapi import APIRouter, Depends, HTTPException
from routers.users import get_current_user
from models import UserInDb, Post, PostInDb
from typing import Annotated
from datetime import datetime, timezone, timedelta


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
        WAT = timezone(timedelta(hours=1))  # West Africa Time
        timestamp = datetime.now(WAT)#stores the time the post is created
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
    
@router.put("/edit/{id}")
def edit_posts(current_user: Annotated[UserInDb, Depends(get_current_user)], post: Post, id: int):
    """a function that edits an existing post"""
    if id in posts.keys():#checks if the post exists
        if (current_user.role.lower() == "author" and current_user.user_name == posts[id]["author"]) or current_user.role.lower() == "admin":
            #checks if the user is an author and if he owns the post or if the user is an admin
            posts[id]["title"] = post.title
            posts[id]["content"] = post.content
            #edits the post
            return ({"message": "Successfully edited post"})
        raise HTTPException(status_code = 403, detail = "UNAUTHORIZED")
    raise HTTPException(status_code = 404, detail = "POST NOT FOUND")

@router.delete("/delete/{id}")
def delete_posts(current_user: Annotated[UserInDb, Depends(get_current_user)], id: int):
    """a function that deletes an existing post"""
    if id in posts.keys():#checks if the post exists
        if (current_user.role.lower() == "author" and current_user.user_name == posts[id]["author"]) or current_user.role.lower() == "admin":
            #checks if the user is an author and if he owns the post or if the user is an admin
            del posts[id]#deletes post
            return({"message": "Successfully deleted post"})
        raise HTTPException(status_code = 403, detail = "UNAUTHORIZED")
    raise HTTPException(status_code = 404, detail = "POST NOT FOUND")

@router.get("/")
def get_all_posts(current_user: Annotated[UserInDb, Depends(get_current_user)], page: int = 1, limit: int = 10):
    """returns all the posts"""
    skip = (page - 1) * limit
    return list(posts.values())[skip: skip + limit]#paginating the posts
    
@router.get("/{id}")
def get_post(current_user: Annotated[UserInDb, Depends(get_current_user)], id: int):
    """returns a particular post"""
    if id in posts.keys():#checks if the post exists
        return posts[id]
    raise HTTPException(status_code = 404, detail = "POST NOT FOUND")