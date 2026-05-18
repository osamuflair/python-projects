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
- Docker

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
- Containerization
    - App is containerized with Docker
    - Image available on Docker Hub

## How to run
- Create a `.env` file with `SECRET_KEY=your_secret_key`
- Install dependencies
- Run `python -m pytest` to run tests first
- Run `uvicorn main:app --reload` to start the server locally
- Or run with Docker: `docker run -p 8000:8000 -e SECRET_KEY=your_secret_key osamuflair/blog-api`
- Or run with Docker Compose: `docker-compose up`