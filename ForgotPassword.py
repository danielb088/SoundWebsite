from nicegui import ui
with ui.row().classes("w-full justify-center gap-5"):
    ui.label("Enter your Email: ").style('font-family: Comic Sans MS; font-size: 37px; font-weight: bold;')
with ui.row().classes("w-full justify-center gap-5"):
<<<<<<< HEAD
    ui.input(placeholder="Email:")
with ui.row().classes("w-full justify-center gap-5"):    
    ui.button("Send code", on_click= lambda: ui.notify("Code sent!!!"))
=======
    ui.input(placeholder="Email")
with ui.row().classes("w-full justify-center gap-5"):    
    ui.button("Send nudes", on_click= lambda: ui.notify("Nudes sent!"))
>>>>>>> ec5b82c9ccad1d3304cd0f6df27936017736e89a
ui.run()