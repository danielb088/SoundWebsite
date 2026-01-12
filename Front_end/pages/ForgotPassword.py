from nicegui import ui

def login_click():
    ui.navigate.to('/')

@ui.page("/ForgotPassword", title= "Forgot pass",favicon="images/logo.png")
def ForgotPassword():    
    ui.colors(primary='#ccf71f')
    with ui.row().classes("w-full justify-center gap-5"):
        ui.label("Enter your Email: ").style('font-family: Comic Sans MS; font-size: 37px; font-weight: bold;')
    with ui.row().classes("w-full justify-center gap-5"):
        ui.input(placeholder="Email:")
    with ui.row().classes("w-full justify-center gap-5"):    
        ui.button("Send code", on_click= lambda: ui.notify("Code sent!!!"))
    with ui.row().classes("w-full justify-center gap-5"): 
        ui.button("back", on_click= login_click)
