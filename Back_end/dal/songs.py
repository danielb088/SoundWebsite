from pymongo import MongoClient
from bunnet import Document
from pydantic import BaseModel
from datetime import datetime
import gridfs
from dal.db import get_db


class Songs(Document):
    user_ID: str
    genre: str

    def add_file(self,file_data,content_type):
        fs = gridfs.GridFS(get_db())
        fs.put(file_data,song_id=str(self.id),contentType=content_type) 

    def get_file(self):
        fs = gridfs.GridFS(get_db())
        data = get_db().fs.files.find_one({'song_id':str(self.id)})
        if data == None:
            return None,None
        
        f_id = data['_id']
        output_data = fs.get(f_id).read()
        return output_data,data['contentType']

    
