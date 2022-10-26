from fastapi import APIRouter,Request
from pydantic import BaseModel
from routes import error_handling
from database import fetcher

# restfull inner api routes for farther application features if needed
# do not check for now,
# this is merly here for later innerserver feature adding.
# note that i left it with my own tests and not something relevent to the test(but comment if you wish so i could adjust it later).

router = APIRouter()

class ClientRequest(BaseModel):
    data: object


@router.get('/options/weather')
async def get():
    weather_list = fetcher.weather_options()
    location_list = fetcher.location_options()
    return {"response": weather_list}

@router.get('/options/location')
async def get():
    location_list = fetcher.location_options()
    return {"response": location_list}

@router.get('/vacation')
async def get(weather: str, location: str):
    print("called")
    if weather != '' and location != '':
        res = fetcher.vacation(weather, location)
    else:
        res = "no query parametrs given"

    return {"response": res}

