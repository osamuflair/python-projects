import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def get_token():
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