import pytest
from fastapi.testclient import TestClient
from main import app
from routers import posts, comments, users

@pytest.fixture(autouse=True)
def reset_state():
    """it resets all the database before each test, to prevent inteference"""
    users.users.clear()
    posts.posts.clear()
    comments.comments.clear()
    yield

@pytest.fixture
def get_token():
    """register and log in user 1"""
    client = TestClient(app)
    client.post("/users/register/", json={
        "user_name": "testuser",
        "email": "test@gmail.com",
        "password": "abc123",
        "role": "Author"
    })
    response = client.post("/token", data={
        "username": "testuser",
        "password": "abc123"
    })
    return response.json()["access_token"]

@pytest.fixture
def get_token2():
    """register and log in user 2"""
    client = TestClient(app)
    client.post("/users/register/", json={
        "user_name": "testuser2",
        "email": "test2@gmail.com",
        "password": "abc123",
        "role": "Admin"
    })
    response = client.post("/token", data={
        "username": "testuser2",
        "password": "abc123"
    })
    return response.json()["access_token"]

@pytest.fixture
def get_token3():
    """register and log in user 3"""
    client = TestClient(app)
    client.post("/users/register/", json={
        "user_name": "testuser3",
        "email": "test3@gmail.com",
        "password": "abc123",
        "role": "Reader"
    })
    response = client.post("/token", data={
        "username": "testuser3",
        "password": "abc123"
    })
    return response.json()["access_token"]

@pytest.fixture
def create_test_post(get_token):
    """create a post for user 1"""
    client = TestClient(app)
    client.post(
        "/posts/",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token}"
        }
    )