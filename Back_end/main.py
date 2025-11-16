from  dal.user import User
from dal.following import Following
from dal.listens import Listens
from dal.songs import Songs
from dal.db import init_db
from fastapi import FastAPI
import uvicorn

from api.user import router as user_router
from api.songs import router as songs_router
from api.listens import router as listens_router
from api.following import router as following


if __name__ == "__main__":
    uvicorn.run("main:app", port=8090,reload=True)
else:
    init_db([User,Following,Listens,Songs])
    app = FastAPI()
    app.include_router(user_router)
