from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime


class Following(Document):
    user_ID: str
    follow_user_ID: str
    
