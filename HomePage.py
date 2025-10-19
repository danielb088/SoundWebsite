from nicegui import ui

with ui.card().style('width: 100%'):
    with ui.row().classes("w-full justify-center gap-5"):
        ui.label("e = mc^2")

ui.run()