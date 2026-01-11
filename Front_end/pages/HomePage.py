from nicegui import ui, app
from requests import get, post

def Filter(row:ui.row, song_name ,genre): 
    data = {"song_name": song_name,"genre": genre}
    response = post('http://127.0.0.1:8090/songs/filter',json=data)
    row.clear()
    with row:
        for song in response.json():
            with ui.card():
                ui.label(song['song_name'])
                ui.label(song['genre'])

def get_all(row:ui.row):
    response = get('http://127.0.0.1:8090/songs/all')
    row.clear()
    with row:
        for u in response.json():
            with ui.card():
                ui.label("name: "+u['song_name'])
                ui.label("genre: "+u['genre'])

def Statistics_click():
    ui.navigate.to('/Statistics')

@ui.page("/HomePage")
def HomePage():
    is_admin = bool(app.storage.user.get("is_admin"))
    user_id = app.storage.user.get("first_name")
    ui.label("hello "+user_id)        
    ui.colors(primary='#ccf71f')
    with ui.card().style('width: 100%'):
        with ui.row().classes("w-full justify-center gap-5"):
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
    with ui.row()as refresh_row:    
        get_all(refresh_row)
    

