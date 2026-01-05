from fastapi import APIRouter,Response,status ,UploadFile

from dal.songs import Songs
from dal.songs import Songs_filter
from dal.user import User

router = APIRouter(prefix="/songs")

@router.get("/all")
def api_get_all():
    return Songs.find().run()

@router.post("")
def api_add(song: Songs):
    if User.get(song.user_ID).run() == None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        song.save()
        return song

# # update
# @router.put("")
# def api_udpate(song: Songs):
#     the_song:Songs = Songs.get(song.id).run() 
#     if the_song == None:
#         return Response(status_code=status.HTTP_404_NOT_FOUND)
#     else:
#         song.save()
#         return song
    

@router.delete("/{song_id}")
def api_delete(song_id: str):
    the_user:Songs = Songs.get(song_id).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        the_user.delete()
        return Response(status_code=status.HTTP_200_OK)

# get specifc song
@router.get("/{song_id}")
def api_get(song_id: str):
    the_song:Songs = Songs.get(song_id).run() 
    if the_song == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return the_song

@router.put("/file/{song_id}")
def api_add_file(song_id: str,upload_file: UploadFile):
    the_song:Songs = Songs.get(song_id).run() 
    if the_song == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    the_song.add_file(upload_file.file, upload_file.content_type)

@router.get("/file/{song_id}")
def api_get_file(song_id: str):
    the_song:Songs = Songs.get(song_id).run() 
    if the_song == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    f_data,media_type = the_song.get_file()
    print(media_type)
    if f_data == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(content=f_data, media_type=media_type)
 
#filter songs
@router.post("/filter")
def api_get_filter(filter:Songs_filter):
    print(filter)
    return Songs.find({"song_name": filter.song_name,"genre":filter.genre}).run()