from nicegui import ui

@ui.page("/HomePage")
def HomePage():        
    with ui.card().style('width: 100%'):
        with ui.row().classes("w-full justify-center gap-5"):
            ui.input(placeholder="Search:")
            ui.label("Sound").style('font-family: Comic Sans MS; font-size: 30px; font-weight: bold;')
    with ui.row().classes("w-full justify-center gap-5"):
        ui.label("Your playlists:")
# with ui.row():

# scroll area

