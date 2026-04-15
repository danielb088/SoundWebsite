from fastapi import APIRouter,Response,status #,UploadFile
from fastapi.responses import JSONResponse

from dal.listens import Listens
from dal.user import User

router = APIRouter(prefix="/listens")

@router.get("/all")
def api_get_all():
    return Listens.find().run()

@router.post("")
def api_add(listen: Listens):
    if User.get(listen.user_ID).run() != None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    valid, error_message = listen.validate_listens()
    if not valid:
        return JSONResponse(content={"error": error_message}, status_code=status.HTTP_409_CONFLICT)
    else:
        listen.save()
        return listen

# update
@router.put("")
def api_udpate(listen: Listens):
    the_listen:Listens = Listens.get(listen.id).run() 
    if the_listen == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    valid, error_message = listen.validate_listens()
    if not valid:
        return JSONResponse(content={"error": error_message}, status_code=status.HTTP_409_CONFLICT)
    else:
        listen.save()
        return listen
    

@router.delete("/{listen_id}")
def api_delete(listen_id: str):
    the_listen:Listens = Listens.get(listen_id).run() 
    if the_listen == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        the_listen.delete()
        return Response(status_code=status.HTTP_200_OK)

# get specifc song
@router.get("/{listen_id}")
def api_get(listen_id: str):
    the_listen:Listens = Listens.get(listen_id).run() 
    if the_listen == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return the_listen