# from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime


# class UserFilter(BaseModel):
#     dob: datetime
#     admin: bool

class UserLogin(BaseModel):
    email: str
    password: str

class User(Document):
    id: str #this is the email
    first_name: str
    last_name: str
    is_admin: bool
    year_b: int
    gender:str
    password: str

