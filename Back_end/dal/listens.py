from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime

class Listens(Document):
    stats_ID: str
    user_ID: str
    time: datetime
    listened_user_ID: str

    def validate_listens(self) -> tuple[bool, str]:
        if not self.stats_ID:
            return False, "stats_ID cannot be empty"
        if not self.user_ID:
            return False, "user_ID cannot be empty"
        if not self.listened_user_ID:
            return False, "listened_user_ID cannot be empty"
        if self.time > datetime.now():
            return False, "listen time cannot be in the future"
        return True, ""

