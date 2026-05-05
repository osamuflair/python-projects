from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_posts(get_token, get_token2, get_token3):
    """tests the posts endpoints"""

    #test for post creation by an author
    response = client.post(
        "/posts/",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "sucessfully created your post"}

    #test for post creation by an admin
    response = client.post(
        "/posts/",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token2}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "sucessfully created your post"}

    #test for post creation by an author
    response = client.post(
        "/posts/",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "sucessfully created your post"}

    #test for post creation by an admin
    response = client.post(
        "/posts/",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token2}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "sucessfully created your post"}

    #test for post creation by an author
    response = client.post(
        "/posts/",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "sucessfully created your post"}

    #test for post creation by a reader
    response = client.post(
        "/posts/",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token3}"
        }
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "UNAUTHORIZED"}


    #test if an author can edit his post
    response = client.put(
        "/posts/edit/1",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully edited post"}

    #test if an author can edit another authors post
    response = client.put(
        "/posts/edit/2",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "UNAUTHORIZED"}

    #test if an admin can edit his post
    response = client.put(
        "/posts/edit/2",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token2}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully edited post"}

    #test if an admin can edit another authors post
    response = client.put(
        "/posts/edit/1",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token2}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully edited post"}

    #test if a reader can edit a post
    response = client.put(
        "/posts/edit/2",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token3}"
        }
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "UNAUTHORIZED"}

    #test to edit a post that does not exists
    response = client.put(
        "/posts/edit/6",
        json = {
            "title": "Test Post",
            "content": "Test content"
        },
        headers = {
            "Authorization": f"Bearer {get_token3}"
        }
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "POST NOT FOUND"}

    #test if an author can delete his post
    response = client.delete(
        "/posts/delete/1",
        headers = {
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully deleted post"}

    #test if an author can delete another authors post
    response = client.delete(
        "/posts/delete/2",
        headers = {
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "UNAUTHORIZED"}

    #test if an admin can delete his post
    response = client.delete(
        "/posts/delete/2",
        headers = {
            "Authorization": f"Bearer {get_token2}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully deleted post"}

    #test if an admin can delete another authors post
    response = client.delete(
        "/posts/delete/3",
        headers = {
            "Authorization": f"Bearer {get_token2}"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully deleted post"}

    #test if a reader can delete a post
    response = client.delete(
        "/posts/delete/4",
        headers = {
            "Authorization": f"Bearer {get_token3}"
        }
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "UNAUTHORIZED"}

    #test to delete a post that does not exists
    response = client.delete(
        "/posts/delete/6",
        headers = {
            "Authorization": f"Bearer {get_token3}"
        }
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "POST NOT FOUND"}




    #test if a post can be gotten by its id
    response = client.get(
        "/posts/5",
        headers={
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 200
    assert response.json()["id"] == 5

    #test if a post that does not exists can be gotten 
    response = client.get(
        "/posts/8",
        headers={
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "POST NOT FOUND"}

    #test to get all post
    response = client.get(
        "/posts/",
        headers={
            "Authorization": f"Bearer {get_token}"
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)