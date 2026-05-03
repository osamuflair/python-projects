# Blog API

## What is This Project
- It is a backend system that powers a blogging platform

## Technologies
- Python
- FastAPI
- PyJWT
- pwdlib
- Thunder Client

## Features
- User management
    - people can register with different roles (admin, author, reader)
- Posts
    - authors write posts
    - everyone can read posts
    - only the author or admin can edit/delete posts
- Comments
    - logged in users can comment on posts
- Pagination
    - posts are returned in pages, not all at once
- Authentication
    - JWT tokens protect the endpoints

## How to run
- Install dependencies
- Run main.py using:
    - uvicorn main:app --reload
- Test end points using Thunder Client