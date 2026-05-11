from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_comments(get_token, get_token2, get_token3, create_test_post):
    """tests the comments end points"""

    #tests if an author can add a comment
    response = client.post(
        "/comment/",
        json = {
            "content": "you fool",
            "post_id": 1
        },
        headers = {
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "sucessfully commented"}

    #tests if an admin can add a comment
    response = client.post(
        "/comment/",
        json = {
            "content": "you fool",
            "post_id": 1
        },
        headers = {
            "Authorization": f"Bearer {get_token2}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "sucessfully commented"}

    #tests if a reader can add a comment
    response = client.post(
        "/comment/",
        json = {
            "content": "you fool",
            "post_id": 1
        },
        headers = {
            "Authorization": f"Bearer {get_token3}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "sucessfully commented"}

    #tests to add comment if a post does not exists
    response = client.post(
        "/comment/",
        json = {
            "content": "you fool",
            "post_id": 2
        },
        headers = {
            "Authorization": f"Bearer {get_token3}"
        }
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "POST NOT FOUND"}

    #tests to get all comments from a post
    response = client.get(
        "/comment/1/",
        headers = {
            "Authorization": f"Bearer {get_token3}"
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)