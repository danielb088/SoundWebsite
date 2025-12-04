from fastapi import status
from fastapi.testclient import TestClient
from main import app
from  dal.user import * 
import random
# from pydantic import TypeAdapter

client = TestClient(app)

# generates a new random user
def generate_user(is_admin)->User:
    id = "email_"+str(random.randint(1, 1000))+"@gmail.com"
    password = "pass_"+str(random.randint(1, 1000))
    f_name = "first_name_"+str(random.randint(1, 1000))
    l_name = "last_name_"+str(random.randint(1, 1000))
    user_dob = datetime(2025,11,18)
    new_user:User = User(id=id,password=password,is_admin=is_admin,dob=user_dob,first_name=f_name,last_name=l_name)
    return new_user



def test_add():
    new_user:User = generate_user(True)
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_user.id
    assert response.json()['password'] == new_user.password
    assert response.json()['first_name'] == new_user.first_name
    assert response.json()['last_name'] == new_user.last_name
    # assert response.json()['dob'] == new_user.dob
    # try to add the same user again, should get 400
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    new_user.delete()


def test_get_all():
    # find how many users are there
    response = client.get("/user/all")
    assert response.status_code == status.HTTP_200_OK
    user_count = len(response.json())

    #create new user
    new_user:User = generate_user(True)
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    
    response = client.get("/user/all")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == user_count+1 #checking that the new user was added

    new_user.delete()

def test_update():
    # generate new user and check that it was added
    new_user:User = generate_user(False)
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    # update the user
    new_user.is_admin = True
    response = client.put("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK
    assert new_user.is_admin

    new_user.delete()


def test_delete():
    # generate new user and check that it was added
    new_user:User = generate_user(True)
    user_id = new_user.id
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    # check user was deleted properly 
    response = client.delete("/user/"+str(user_id))
    assert response.status_code == status.HTTP_200_OK
    response = client.get("/user/"+str(user_id))
    assert response.status_code == status.HTTP_404_NOT_FOUND

    new_user.delete()


def test_get_single():   #### NEED TO TEST
    # add user
    new_user:User = generate_user(True)
    user_id = new_user.id
    response = client.post("/user",data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    response = client.get("/user/"+str(user_id))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['_id'] == new_user.id

def test_login():
    new_user:User = generate_user(True)
    response = client.post("/user", data=new_user.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    ul:UserLogin = UserLogin(email = new_user.id, password=new_user.password)
    
    response = client.post("/user/login", data=ul.model_dump_json())
    assert response.status_code == status.HTTP_200_OK

    ul_1:UserLogin = UserLogin(email = "asdasd", password = "123")
    response = client.post("/user/login", data=ul_1.model_dump_json())
    assert response.status_code == status.HTTP_404_NOT_FOUND

    ul_2:UserLogin = UserLogin(email = new_user.id, password = "123")
    response = client.post("/user/login", data=ul_2.model_dump_json())
    assert response.status_code == status.HTTP_404_NOT_FOUND




# def test_get_filter():
#     # add a new Male admin user 
#     new_user1:User = generate_user("M",True)
#     response = client.post("/user",data=new_user1.model_dump_json())
#     assert response.status_code == status.HTTP_200_OK
#     # add a new FeMale admin user 
#     new_user2:User = generate_user("F",True)
#     response = client.post("/user",data=new_user2.model_dump_json())
#     assert response.status_code == status.HTTP_200_OK
#     # add a new Male not admin user 
#     new_user3:User = generate_user("M",False)
#     response = client.post("/user",data=new_user3.model_dump_json())
#     assert response.status_code == status.HTTP_200_OK
#     # add a new Female not admin user 
#     new_user4:User = generate_user("F",False)
#     response = client.post("/user",data=new_user4.model_dump_json())
#     assert response.status_code == status.HTTP_200_OK

#     # check Male Admin filter
#     uf:UserFilter = UserFilter(gender="M",admin=True)
#     response = client.post("/user/filter",data=uf.model_dump_json())
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.json()) > 0
#     for d in response.json():
#         assert d["gender"] == "M"
#         assert d["admin"] == True

#     # TODO: check other filter options


#     new_user1.delete()
#     new_user2.delete()
#     new_user3.delete()
#     new_user4.delete()