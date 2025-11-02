from dal.user import User
from dal.following import Following
from dal.listens import Listens
from dal.songs import Songs
from bunnet import init_bunnet
from pymongo import MongoClient

def connect2db():
    print("connecting to DB...")
    client = MongoClient("mongodb+srv://raz:raz@cluster0.mzxtq.mongodb.net/")
    init_bunnet(database=client.Music, document_models=[User,Songs,Listens,Following])
    print("connected to DB.")
    return client.Music