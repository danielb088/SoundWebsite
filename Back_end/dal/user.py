# from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime


class UserFilter(BaseModel):
    dob: datetime
    admin: bool

class UserLogin(BaseModel):
    user_name: str
    password: str

class User(Document):
    id: str #this
    first_name: str
    last_name: str
    is_admin: bool
    dob: datetime
    password: str

