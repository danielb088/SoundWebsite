from nicegui import ui

def HomePage_click(): 
    ui.navigate.to('/HomePage')

@ui.page('/Statistics')
def Statistics():
    ui.colors(primary='#ccf71f')
    ui.echart({
    'xAxis': {'type': 'value'},
    'yAxis': {'type': 'category', 'data': ['A', 'B'], 'inverse': True},
    'legend': {'textStyle': {'color': 'gray'}},
    'series': [
        {'type': 'bar', 'name': 'Current year', 'data': [0.1, 0.2]},
        {'type': 'bar', 'name': 'Last year', 'data': [0.3, 0.4]},
    ],
    })

    with ui.row().classes('w-full justify-center'):
        ui.button("Back", on_click=HomePage_click)