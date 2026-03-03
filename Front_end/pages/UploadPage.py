from nicegui import ui, app
from requests import get, post, delete, put
from asyncio import sleep

async def upload_song(user_id, genre, song_name, duration):
    data = {"user_ID": user_id, "genre": genre, "song_name": song_name, "duration": duration}
    response = post('http://127.0.0.1:8090/songs',json= data)
    song_id = response.json()['_id']
    await upload_file(song_id) # await a second time so the website can continue without stopping
    ui.navigate.to("/HomePage")

async def upload_file(song_id):
    file_name = file_data.name
    file_content = await file_data.read()
    content_type = file_data.content_type
    print(file_name,content_type)
    put('http://127.0.0.1:8090/songs/file/'+song_id, files = {"file": (file_name , file_content, content_type)})


def update_file(event):
    global file_data
    file_data = event.file


@ui.page("/UploadPage", title= "upload song",favicon="images/logo.png")
def UploadPage():
    user_id = app.storage.user.get("first_name")
    with ui.row().classes("w-full justify-center gap-5"):
        ui.label(text= "Upload Song")
    with ui.row().classes("w-full justify-center gap-5"):
        name = ui.input(placeholder = "name")
        genre = ui.input(placeholder = "genre")
        duration = ui.input(placeholder = "duration (seconds)")#TRY TO FIND DURATION TRHOUGH THE FILE DATA INSTEAD OF ASKING THE USER
        ui.upload(label="add song file",on_upload = lambda event: update_file(event),auto_upload=True,max_files=1)
        ui.button('upload',on_click= lambda: upload_song(user_id, genre.value, name.value, duration.value))

