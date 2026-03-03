from bunnet import Document
from pydantic import BaseModel
from datetime import datetime

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

    def validate_user(self) -> tuple[bool, str]:
        if self.gender not in ["Male", "Female", "Other"]:
            return False, "Gender must be Male, Female or Other"

        if len(self.password) < 5:
            return False, "Password must be at least 5 characters"
        
        if '@' not in self.id:
            return False, "an Email adress must contain '@' sign"
        
        return True, ""
