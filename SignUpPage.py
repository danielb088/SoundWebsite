from random import randint
from nicegui import ui
import re

#check
#regex validation: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ 

#random color slider:
# ui.slider(min=0, max=10, step=0.1, value=5).props('label-always').on('update:model-value', lambda e: ui.colors(primary=f'#{randint(0, 0xffffff):06x}'),
#         throttle=0.01, trailing_events=False))


with ui.row().classes("w-full justify-center gap-5"):
    ui.label("SoundNimbostratus").style('font-family: Comic Sans MS; font-size: 37px; font-weight: bold;')
    ui.icon('savings', color='primary').classes('text-5xl')
    with ui.row().classes("w-full justify-center"): 
        with ui.column().classes():     
            ui.input(placeholder="Enter your first name")
            ui.input(placeholder="Enter your last name")
            ui.number(label ="Enter your age",value= 0,validation={"Age needs to be between 0 and 120": lambda value: 0 < value < 120})  
        with ui.column().classes():
            ui.input(placeholder="Enter your email",validation={"need to contain @gmail.com": lambda value: "@gmail.com" in value})
            ui.input(placeholder="Enter your password",password=True,password_toggle_button=True)
            ui.input(placeholder="Enter your password again",password_toggle_button=True)   
    with ui.row().classes():
        with ui.dropdown_button('Select your gender', auto_close=True):
                ui.item('Male', on_click=lambda: ui.notify('You clicked Male'))
                ui.item('Female', on_click=lambda: ui.notify('You clicked Female'))
                ui.item('Other', on_click=lambda: ui.notify('You clicked Other'))
    ui.button('Sign up', on_click=lambda: ui.notify('You are now signed up!'))

ui.run()

            