from nicegui import ui

from requests import get
from fastapi import status

def login_click():
    ui.navigate.to('/')

def send_password(user_id):
    response = get('http://127.0.0.1:8090/user'+user_id)
    if response == status.HTTP_404_NOT_FOUND:
        print("error in sending email")
    else:
        ui.notify("passsward sent!!!")
        
    

@ui.page("/ForgotPassword", title= "Forgot pass",favicon="images/logo.png")
def ForgotPassword():
    ui.colors(primary='#ccf71f')
    with ui.row().classes("w-full justify-center gap-5"):
        ui.label("Enter your Email: ").style('font-family: Comic Sans MS; font-size: 37px; font-weight: bold;')
    with ui.row().classes("w-full justify-center gap-5"):
        user_id = ui.input(placeholder="Email:")
    with ui.row().classes("w-full justify-center gap-5"):    
        ui.button("Send password", on_click= send_password)
    with ui.row().classes("w-full justify-center gap-5"): 
        ui.button("back", on_click= login_click)
