from nicegui import ui
with ui.row().classes("w-full justify-center gap-5"):
    ui.label("Enter your Email: ").style('font-family: Comic Sans MS; font-size: 37px; font-weight: bold;')
with ui.row().classes("w-full justify-center gap-5"):
    ui.input(placeholder="Email")
with ui.row().classes("w-full justify-center gap-5"):    
    ui.button("Send nudes", on_click= lambda: ui.notify("Nudes sent!"))
ui.run()