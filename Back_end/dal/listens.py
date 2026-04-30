from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime

class Listens(Document):
    user_ID: str
    time: datetime
    song_ID: str    