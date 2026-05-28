![CI/CD](https://github.com/osamuflair/python-projects/actions/workflows/main.yml/badge.svg)

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
    - Automated tests run on every push via GitHub Actions
- Containerization
    - App is containerized with Docker
    - Image available on Docker Hub
- CI/CD
    - GitHub Actions automatically tests and builds Docker image on every push

## How to run
- Create a `.env` file with `SECRET_KEY=your_secret_key`
- Install dependencies
- Run `python -m pytest` to run tests locally
- Run `uvicorn main:app --reload` to start the server locally
- Or run with Docker: `docker run -p 8000:8000 -e SECRET_KEY=your_secret_key osamuflair/blog-api`
- Or run with Docker Compose: `docker-compose up`

## Live Demo
- API: https://blog-api-0gae.onrender.com/docs