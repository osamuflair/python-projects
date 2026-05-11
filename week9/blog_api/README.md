# Blog API

## What is This Project
- It is a backend system that powers a blogging platform

## Technologies
- Python
- FastAPI
- PyJWT
- pwdlib
- pytest
- httpx
- python-dotenv

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
- Testing

## How to run
- Create a `.env` file with `SECRET_KEY=your_secret_key`
- Install dependencies
- Run `uvicorn main:app --reload` to start the server
- Run `python -m pytest` to run tests
