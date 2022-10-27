from fastapi import APIRouter, Response
from pydantic import BaseModel
from routes import error_handling
from apis.my_outsource_api import MyOutsourceApi

EXTERNAL_PLAYERS_API_BASE_URL = "https://recipes-goodness.herokuapp.com/"
router = APIRouter()
caching_dreamteam = {}

class Hotel(BaseModel):
    id: int
    name: str
    location: str
    thumbnail: str

@router.get('/hotels')
def get_players(response: Response, location="", date=""):
    response.headers['Access-Control-Allow-Origin'] = "*"
    # caching_metadata = MyOutsourceApi(EXTERNAL_PLAYERS_API_BASE_URL).make_call("GET", f"recipes/{ingredient}").proccess_data(gluten, dairy)
    hotels = [{"id": i, "name":"Trump", "location":"London", "thumbnail":""} for i in range(3)]
    result = {"response": hotels}

    return result


@router.get('/favorites')
def get(response: Response):
    global caching_dreamteam
    return list(caching_dreamteam.values())

@router.post('/favorites')
def post(data: Hotel):
    global caching_dreamteam
    data.dreamTeam = True
    caching_dreamteam[data.id] = data
    return data

@router.put('/favorites')
def put(data: Hotel):
    global caching_dreamteam
    data.dreamTeam = True
    caching_dreamteam[data.id] = data
    return data

@router.delete('/favorites/{id}')
def delete(id):
    global caching_dreamteam
    id=int(id)
    player = caching_dreamteam[id]
    del caching_dreamteam[id]
    player.dreamTeam = False
    return player


# note: later on add all CRUD operations