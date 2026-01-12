from nicegui import ui, app

import HomePage
import SignUpPage
import ForgotPassword
import Statistics

from requests import post
from fastapi import status

def forgot_pass_click():
    ui.navigate.to('/ForgotPassword')

def SignUp_click(): 
    ui.navigate.to('/SignUp')

def HomePage_click(email,password):
    data = {"email": email,"password": password}
    response = post("http://127.0.0.1:8090/user/login",json=data)
    if response.status_code == status.HTTP_200_OK:
        app.storage.user.update({"user_id":response.json()['_id']})
        app.storage.user.update({"first_name":response.json()['first_name']})
        app.storage.user.update({"is_admin":response.json()['is_admin']})
        ui.navigate.to('/HomePage')
    else:
        ui.notify("invlaid email or password")

@ui.page('/',title="my login page",favicon="images/logo.png")
def show_page():
    with ui.row().classes("w-full justify-center"):
        ui.colors(primary='#ccf71f')
        ui.image("images/logo.png").classes("w-32")

    with ui.row().classes("w-full justify-center gap-5"):
        ui.label("Log in").style('font-family: Comic Sans MS; font-size: 37px; font-weight: bold;')
    with ui.row().classes("w-full justify-center gap-5"):
        with ui.column():
                username = ui.input(placeholder="Enter your email")
                password = ui.input(placeholder="Enter your password", password=True)

    with ui.row().classes("w-full justify-center gap-5"):
        ui.button('Log in', on_click=lambda:HomePage_click(username.value,password.value))
        ui.button('Sign up', on_click=SignUp_click)
    with ui.row().classes("w-full justify-center gap-5"):
        ui.button('Forgot password', on_click=lambda: forgot_pass_click())
    # with ui.div(style="position: fixed; bottom: 0; left: 0;"):
    # with ui.dropdown_button(auto_close=True):
    ui.slider(min=0, max=100, value=50)
ui.run(storage_secret="TheBigStien")
