from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime

class User(Document):
    id: str #this
    f_name: str
    l_name: str
    is_admin: bool
    dob: datetime
    password: str