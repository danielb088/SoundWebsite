from fastapi import APIRouter,Response,status,UploadFile

from dal.user import User

router = APIRouter(prefix="/user")


# # find all users
@router.get("/all")
def api_get_all():
    return User.find().run()
