from  dal.user import User
from dal.following import Following
from dal.listens import Listens
from dal.songs import Songs
from dal.db import init_db
from fastapi import FastAPI
import uvicorn
from api.user import router as user_router


if __name__ == "__main__":
    uvicorn.run("main:app", port=8090,reload=True)
else:
    init_db([User,Following,Listens,Songs])
    app = FastAPI()
    app.include_router(user_router)
