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
    # hotels = [{"id": i, "name":"Trump", "location":"London", "thumbnail":""} for i in range(3)]
    hotels = [{"id": 1, "name": "the tower hotel",
    "location": "St Katharine's Way, Tower Hamlets, London, UK",
    "thumbnail": "https://image-tc.galaxy.tf/wijpeg-csh4w01i79s0j1kyasp6kxzji/view-of-the-tower-1.jpg",
    "dreamTeam": False},
    {"id": 2,
    "name": "Leonardo Royal Hotel London Tower Bridge",
    "location": "45 Prescot Street, London, UK",
    "thumbnail": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/23/70/4c/56/swimming-pool.jpg?w=700&h=-1&s=1",
    "dreamTeam": False},
    {"id": 3,
    "name": "Leonardo Royal Hotel London St Paul",
    "location": "10 Godliman Street, London, UK",
    "thumbnail": "https://pix8.agoda.net/hotelImages/168893/-1/76532aa1b26c9339837a1a0c1bdff332.jpg?ca=16&ce=1&s=1024x768",
    "dreamTeam": False},
    {"id": 4,
    "name": "The Savoy Hotel",
    "location": "200 Westminster Bridge Road, London, UK",
    "thumbnail": "https://pix8.agoda.net/hotelImages/9456764/0/96bf6f148c9d281bde0c2a813ddd4d87.jpg?ca=9&ce=1&s=1024x768",
    "dreamTeam": False},
    {"id": 5,
    "name": "Park Plaza Westminster Bridge Hotel",
    "location": "Strand, WC2R 0EU, London, UK",
    "thumbnail": "https://pix8.agoda.net/hotelImages/11070/-1/a240812e5fddf294f2eb874a95ee0b9f.jpg?ca=7&ce=1&s=1024x768",
    "dreamTeam": False}
    ]
    result = {"response": hotels}
    return result
0

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