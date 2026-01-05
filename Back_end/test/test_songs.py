from fastapi import status
from fastapi.testclient import TestClient
from main import app
from  dal.songs import * 
from  dal.user import *
import random
# from pydantic import TypeAdapter

client = TestClient(app)

def generate_user(is_admin)->User:
    id = "email_"+str(random.randint(1, 1000))+"@gmail.com"
    password = "pass_"+str(random.randint(1, 1000))
    f_name = "first_name_"+str(random.randint(1, 1000))
    l_name = "last_name_"+str(random.randint(1, 1000))
    user_dob = datetime(2025,11,18)
    new_user:User = User(id=id,password=password,is_admin=is_admin,dob=user_dob,first_name=f_name,last_name=l_name)
    return new_user

def generate_song():
    new_user:User = generate_user(True)
    new_user.save()
    user_id = new_user.id
    song_genre = "heavy_"+str(random.randint(1,1000))
    new_song:Songs = Songs(user_ID = user_id, genre = song_genre)

    return new_song


def test_get_all():
    # find how many songs are there
    response = client.get("/songs/all")
    assert response.status_code == status.HTTP_200_OK
    song_count = len(response.json())

    #create new song
    new_song:Songs = generate_song()
    response = client.post("/songs",data=new_song.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    
    response = client.get("/songs/all")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == song_count+1 #checking that the new song was added

    new_song.delete()

def test_add():
    new_song:Songs = generate_song()
    response = client.post("/songs",data=new_song.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_song.id
    assert response.json()['user_ID'] == new_song.user_ID
    assert response.json()['genre'] == new_song.genre
    
    # try to add the same song again, should get 400
    response = client.post("/songs",data=new_song.model_dump_json())
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    new_song.delete()

def test_delete():
    # generate new song and check that it was added
    new_song:Songs = generate_song()
    song_id = new_song.id
    response = client.post("/songs",data=new_song.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    # check song was deleted properly 
    response = client.delete("/songs/"+str(song_id))
    assert response.status_code == status.HTTP_200_OK
    response = client.get("/songs/"+str(song_id))
    assert response.status_code == status.HTTP_404_NOT_FOUND

    new_song.delete()

def test_get_single():   
    # add song
    new_song:Songs = generate_song()
    song_id = new_song.id
    response = client.post("/songs",data=new_song.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    response = client.get("/songs/"+str(song_id))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_song.id


# def test_add_file():
