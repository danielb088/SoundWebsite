from nicegui import ui

def Statistics_click():
    ui.navigate.to('/Statistics')

@ui.page("/HomePage")
def HomePage():        
    ui.colors(primary='#ccf71f')
    with ui.card().style('width: 100%'):
        with ui.row().classes("w-full justify-center gap-5"):
            ui.button("Statistics", on_click=Statistics_click)
            ui.input(placeholder="Search:")
            ui.label("Sound").style('font-family: Comic Sans MS; font-size: 30px; font-weight: bold;')
    with ui.row().classes("w-full justify-center gap-5"):
        ui.label("Your playlists:")
    
# with ui.row():

# scroll area

