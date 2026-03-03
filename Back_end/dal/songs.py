from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime
import gridfs
from dal.db import get_db

class Songs_filter(BaseModel):
    genre: str
    song_name: str


class Songs(Document):
    user_ID: str
    genre: str
    song_name: str
    duration: int
    
    def validate_song(self) -> tuple[bool, str]:
        if len(self.song_name) < 2: 
            return False, "the Songs name is too short" 
        if self.duration < 15:
            return False, "the song is too short"
        True, ""

    def add_file(self,file_data,content_type):
        fs = gridfs.GridFS(get_db())
        fs.put(file_data,song_id=str(self.id),contentType=content_type) 

    def get_file(self):
        fs = gridfs.GridFS(get_db())
        print("id: "+str(self.id))
        data = get_db().fs.files.find_one({'song_id':str(self.id)})
        print(data) # TEMP
        if data == None:
            return None,None
        
        f_id = data['_id']
        output_data = fs.get(f_id).read()
        return output_data,data['contentType']
    
    def delete_file(self):
        fs = gridfs.GridFS(get_db())
        data = get_db().fs.files.find_one({'song_id':str(self.id)})

        f_id = data['_id']

        fs.delete(f_id)

    

    
