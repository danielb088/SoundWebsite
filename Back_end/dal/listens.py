from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime

class Listens(Document):
    stats_ID: str
    user_ID: str
    time: datetime
    listened_user_ID: str
