from random import randint
from nicegui import ui, app
from requests import post
from fastapi import status



#check
#regex validation: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ 

#random color slider:
# ui.slider(min=0, max=10, step=0.1, value=5).props('label-always').on('update:model-value', lambda e: ui.colors(primary=f'#{randint(0, 0xffffff):06x}'),
#         throttle=0.01, trailing_events=False))
def HomePage_click(): 
    ui.navigate.to('/HomePage')

def Gender(gender):
    ui.notify('You clicked '+str(gender))
    

def SignUp_click(email, f_name, l_name, year_b, password, gender): 
    data = {"_id": email, "first_name": f_name, "last_name": l_name, "is_admin": False, "year_b": year_b,"gender": gender ,"password": password}
    response = post("http://127.0.0.1:8090/user", json=data)
    if response.status_code == status.HTTP_200_OK:
        app.storage.user.update({"user_id":response.json()['_id']})
        app.storage.user.update({"first_name":response.json()['first_name']})
        app.storage.user.update({"is_admin":response.json()['is_admin']})
        ui.navigate.to("/HomePage")


@ui.page("/SignUp")
def SignUp():
    ui.colors(primary='#ccf71f')
    with ui.row().classes("w-full justify-center gap-5"):
        with ui.card().tight():     
            ui.label("SoundNimbostratus").style('font-family: Comic Sans MS; font-size: 37px; font-weight: bold;')
            ui.icon('savings', color='primary').classes('text-5xl')
        with ui.row().classes("w-full justify-center"): 
            with ui.column().classes():     
                f_name = ui.input(placeholder="Enter your first name")
                l_name = ui.input(placeholder="Enter your last name")
            with ui.column().classes():
                email = ui.input(placeholder="Enter your email",validation={"need to contain @gmail.com": lambda value: "@gmail.com" in value})
                password = ui.input(placeholder="Enter your password",password=True,password_toggle_button=True)
                ui.input(placeholder="Enter your password again", password=True,password_toggle_button=True)   
        with ui.row().classes():
            gender = ui.select(["Male","Female","Other"], label="Gender")
            year_b = ui.select(list(range(1970,2026)), label="Year of birth")
        ui.button('Sign up', on_click=lambda: SignUp_click(email= str(email.value), f_name= str(f_name.value), l_name= str(l_name.value),year_b= year_b.value, gender=gender.value, password= str(password.value)))

            