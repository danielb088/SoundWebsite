from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime


class Songs(Document):
    user_ID: str
    genre: str
    
