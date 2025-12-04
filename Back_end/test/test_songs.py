from fastapi import status
from fastapi.testclient import TestClient
from main import app
from  dal.songs import * 
from  dal.user import *
import random
# from pydantic import TypeAdapter

client = TestClient(app)

def generate_user(is_admin)->User:
    id = "email_"+str(random.randint(1, 1000))+"@gmail.com"
    password = "pass_"+str(random.randint(1, 1000))
    f_name = "first_name_"+str(random.randint(1, 1000))
    l_name = "last_name_"+str(random.randint(1, 1000))
    user_dob = datetime(2025,11,18)
    new_user:User = User(id=id,password=password,is_admin=is_admin,dob=user_dob,first_name=f_name,last_name=l_name)
    return new_user

def generate_song():
    new_user:User = generate_user(True)
