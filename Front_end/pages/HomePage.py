from nicegui import ui, app
from requests import get, post, delete, put
from asyncio import sleep
from datetime import datetime

def delete_song(id):
    delete('http://127.0.0.1:8090/songs/'+id)
    delete('http://127.0.0.1:8090/songs/file/'+id)
    ui.navigate.to("/HomePage")

def add_listen(user_id, song_id):
    data = {"user_ID": str(user_id), "time": str((datetime.now())), "song_ID": str(song_id)}
    post('http://127.0.0.1:8090/listens', json=data)


def Filter(row:ui.row, song_name ,genre): 
    is_admin = bool(app.storage.user.get("is_admin"))
    user_id = str(app.storage.user.get("user_id"))
    data = {"song_name": song_name,"genre": genre}
    response = post('http://127.0.0.1:8090/songs/filter',json=data)
    row.clear()
    with row:
        for song in response.json():
            song_id = song['_id']
            with ui.card():
                ui.label(song['song_name'])
                ui.label(song['genre'])
                Audio = ui.audio('http://127.0.0.1:8090/songs/file/'+song_id)
                Audio.on('play', lambda : add_listen(user_id, song_id))
                if is_admin:
                    ui.button('delete', on_click = lambda: delete_song(song_id))
                
def get_all(row:ui.row):
    is_admin = bool(app.storage.user.get("is_admin"))
    user_id = str(app.storage.user.get("user_id"))
    response = get('http://127.0.0.1:8090/songs/all')
    row.clear()
    with row:
        for song in response.json():
            song_id = song['_id']
            with ui.card():
                ui.label("name: "+song['song_name'])
                ui.label("genre: "+song['genre'])
                Audio = ui.audio('http://127.0.0.1:8090/songs/file/'+song_id)
                Audio.on('play', lambda : add_listen(user_id, song_id))
                if is_admin:
                    ui.button('delete', on_click= lambda:delete_song(song_id))

def Statistics_click():
    ui.navigate.to('/Statistics')

def Upload_click():
    ui.navigate.to("/UploadPage")

@ui.page("/HomePage", title= "Home",favicon="images/logo.png")
def HomePage():
    is_admin = bool(app.storage.user.get("is_admin"))
    name_user = app.storage.user.get("first_name")
    ui.label("hello "+name_user)        
    ui.colors(primary='#ccf71f')
    with ui.card().style('width: 100%'):
        with ui.row().classes("w-full justify-center gap-5"):
            if is_admin:
                ui.button("Statistics", on_click=Statistics_click)
            ui.input(placeholder="Search:")
            ui.label("Sound").style('font-family: Comic Sans MS; font-size: 30px; font-weight: bold;')
    with ui.row().classes("w-full justify-center gap-5"):
        ui.label("Your songs:")
    with ui.row():
        song_name_input = ui.input('song name')
        genre_input =ui.input("genre")
        ui.button('Filter',on_click=lambda:Filter(refresh_row,str(song_name_input.value),str(genre_input.value)))
        ui.button('Clear',on_click=lambda:get_all(refresh_row))
        ui.button('Upload song', on_click= Upload_click)
    with ui.row()as refresh_row:    
        get_all(refresh_row)
    

