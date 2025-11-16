from fastapi import APIRouter,Response,status #,UploadFile

from dal.user import User,UserLogin,UserFilter

router = APIRouter(prefix="/user")

# Find all users
@router.get("/all")
def api_get_all():
    return User.find().run()

# Add user
@router.post("")
def api_add(user: User):
    if User.get(user.id).run() != None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        user.save()
        return user

# update
@router.put("")
def api_udpate(user: User):
    the_user:User = User.get(user.id).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        user.save()
        return user
    

@router.delete("/{user_id}")
def api_delete(user_id: str):
    the_user:User = User.get(user_id).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        the_user.delete()
        return Response(status_code=status.HTTP_200_OK)

# get specifc user 
@router.get("/{user_id}")
def api_get(user_id: str):
    the_user:User = User.get(user_id).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return the_user


# Login
@router.post("/login")
def api_login(ul: UserLogin) :
    the_user:User = User.get(ul.user_name).run() 
    if the_user == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    elif the_user.password != ul.password:
        return Response(status_code=status.HTTP_404_NOT_FOUND)        
    else:
        return the_user
    
# Filter users
@router.post("/filter")
def api_get_filter(filter:UserFilter):
    return User.find({'dob':filter.dob,'admin':filter.admin}).run()