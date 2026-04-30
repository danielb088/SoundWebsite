from nicegui import ui, app
from requests import get

def HomePage_click(): 
    ui.navigate.to('/HomePage')

@ui.page('/Statistics', title= "statistics",favicon="images/logo.png")
def Statistics():
    name_user = app.storage.user.get("first_name")
    ui.label("hello "+name_user)        
    with ui.card().style('width: 100%'):
        with ui.row().classes("w-full justify-center gap-5"):
            ui.label("Statistics").style('font-family: Comic Sans MS; font-size: 30px; font-weight: bold;')
    result = get('http://127.0.0.1:8090/listens/all')
    grid = ui.aggrid({
                    'columnDefs': [
                        {'headerName': 'user_id', 'field': 'user_ID','filter':True},
                        {'headerName': 'time', 'field': 'time'},
                        {'headerName': 'song_id', 'field': 'song_ID'},
                    ],
                    'rowData': result.json() 
                },theme='balham')
        