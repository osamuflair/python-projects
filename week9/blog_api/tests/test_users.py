import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_user():
    """tests the users endpoints"""
    
    #test for user registration
    response = client.post(
        "/users/register/",
        json={
            "user_name": "Osamu",
            "email": "osamu21@gmail.com",
            "password": "abc123",
            "role": "Admin"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"Message": "Successfully Registered"}

    #tests if the same username can be used multiple times for registration
    response = client.post(
        "/users/register/",
        json={
            "user_name": "Osamu",
            "email": "osamu21@gmail.com",
            "password": "abc12366",
            "role": "Author"
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}

    #tests for correct credential log-in
    response = client.post(
            "/token",
            data={
                "username": "Osamu",
                "password": "abc123"
            }
        )
    assert response.status_code == 200
    token = response.json()["access_token"]
    assert token is not None
    assert len(token) > 0

    #tests for wrong credential log-in
    response = client.post(
            "/token",
            data={
                "username": "Osamu",
                "password": "abc123hy4"
            }
        )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}