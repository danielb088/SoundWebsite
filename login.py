from nicegui import ui

with ui.row().classes("w-full justify-center gap-5"):
    ui.label("Log in").style('font-family: Comic Sans MS; font-size: 37px; font-weight: bold;')
with ui.row().classes("w-full justify-center gap-5"):
    with ui.column():
            ui.input(placeholder="Enter your first name")
            ui.input(placeholder="Enter your last name")

with ui.row().classes("w-full justify-center gap-5"):
    ui.button('Log in')
    ui.button('Sign up', on_click=lambda: ui.notify('You are now signed up!'))
with ui.row().classes("w-full justify-center gap-5"):
    ui.button('Forgot password', on_click=lambda: ui.notify('You are now signed up!'))
ui.slider(min=0, max=100, value=50)
ui.run()
