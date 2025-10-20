from nicegui import ui

import HomePage
import SignUpPage
import ForgotPassword
import Statistics

def SignUp_click(): 
    ui.navigate.to('/SignUp')

def HomePage_click(): 
    ui.navigate.to('/HomePage')

@ui.page('/',title="my login page")
def show_page():
    ui.colors(primary='#ccf71f')

    with ui.row().classes("w-full justify-center gap-5"):
        ui.label("Log in").style('font-family: Comic Sans MS; font-size: 37px; font-weight: bold;')
    with ui.row().classes("w-full justify-center gap-5"):
        with ui.column():
                ui.input(placeholder="Enter your first name")
                ui.input(placeholder="Enter your last name")

    with ui.row().classes("w-full justify-center gap-5"):
        ui.button('Log in', on_click=HomePage_click)
        ui.button('Sign up', on_click=SignUp_click)
    with ui.row().classes("w-full justify-center gap-5"):
        ui.button('Forgot password', on_click=lambda: ui.notify('You are now signed up!'))
    # with ui.div(style="position: fixed; bottom: 0; left: 0;"):
    # with ui.dropdown_button(auto_close=True):
    ui.slider(min=0, max=100, value=50)
ui.run()
