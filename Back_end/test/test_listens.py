from fastapi import status
from fastapi.testclient import TestClient
from main import app
from dal.listens import Listens
from dal.user import User
from datetime import datetime
import random

client = TestClient(app)

def generate_user() -> User:
    id = "email_" + str(random.randint(1, 1000)) + "@gmail.com"
    password = "pass_" + str(random.randint(1, 1000))
    f_name = "first_name_" + str(random.randint(1, 1000))
    l_name = "last_name_" + str(random.randint(1, 1000))
    user_dob = datetime(2025, 11, 18)
    return User(id=id, password=password, is_admin=False, dob=user_dob, first_name=f_name, last_name=l_name)

def generate_listen() -> tuple[Listens, User]:
    new_user = generate_user()
    new_user.save()
    song_id = "song_" + str(random.randint(1, 100000))
    listen = Listens(user_ID=new_user.id, time=datetime(2025, 11, 18, 12, 0, 0), song_ID=song_id)
    return listen, new_user


def test_add():
    listen, user = generate_listen()
    response = client.post("/listens", data=listen.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["user_ID"] == listen.user_ID
    assert response.json()["song_ID"] == listen.song_ID

    # adding a listen with a non-existent user should fail
    bad_listen = Listens(user_ID="nonexistent@user.com", time=datetime(2025, 11, 18), song_ID="song_999")
    response = client.post("/listens", data=bad_listen.model_dump_json())
    assert response.status_code == status.HTTP_404_NOT_FOUND

    listen.delete()
    user.delete()


def test_get_all():
    response = client.get("/listens/all")
    assert response.status_code == status.HTTP_200_OK
    listen_count = len(response.json())

    listen, user = generate_listen()
    response = client.post("/listens", data=listen.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    response = client.get("/listens/all")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == listen_count + 1

    listen.delete()
    user.delete()


def test_get_single():
    listen, user = generate_listen()
    response = client.post("/listens", data=listen.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    listen_id = response.json()["_id"]

    response = client.get("/listens/" + listen_id)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["_id"] == listen_id
    assert response.json()["user_ID"] == listen.user_ID

    # non-existent listen should return 404
    response = client.get("/listens/000000000000000000000000")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    listen.delete()
    user.delete()


def test_update():
    listen, user = generate_listen()
    response = client.post("/listens", data=listen.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    listen_id = response.json()["_id"]

    # update the song_ID
    updated_listen = Listens(
        id=listen_id,
        user_ID=listen.user_ID,
        time=listen.time,
        song_ID="updated_song_" + str(random.randint(1, 1000))
    )
    response = client.put("/listens", data=updated_listen.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["song_ID"] == updated_listen.song_ID

    updated_listen.delete()
    user.delete()


def test_delete():
    listen, user = generate_listen()
    response = client.post("/listens", data=listen.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    listen_id = response.json()["_id"]

    response = client.delete("/listens/" + listen_id)
    assert response.status_code == status.HTTP_200_OK

    response = client.get("/listens/" + listen_id)
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # deleting a non-existent listen should return 404
    response = client.delete("/listens/000000000000000000000000")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    user.delete()
