from fastapi import APIRouter,Response,status #,UploadFile

from dal.following import Following

router = APIRouter(prefix="/following")

@router.get("/all")
def api_get_all():
    return Following.find().run()

@router.post("")
def api_add(follow: Following):
    if Following.get(follow.id).run() != None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        follow.save()
        return follow

# update
@router.put("")
def api_udpate(follow: Following):
    the_follow:Following = Following.get(follow.id).run() 
    if the_follow == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        follow.save()
        return follow
    

@router.delete("/{follow_id}")
def api_delete(follow_id: str):
    the_follow:Following = Following.get(follow_id).run() 
    if the_follow == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        the_follow.delete()
        return Response(status_code=status.HTTP_200_OK)

# get specifc follow
@router.get("/{follow_id}")
def api_get(follow_id: str):
    the_follow:Following = Following.get(follow_id).run() 
    if the_follow == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return the_follow
    