from fastapi import APIRouter,Request
from pydantic import BaseModel
from routs import error_handling
from database import db_queries

# restfull inner api routs for farther application features if needed
# do not check for now,
# this is merly here for later innerserver feature adding.
# note that i left it with my own tests and not something relevent to the test(but comment if you wish so i could adjust it later).

router = APIRouter()
caching_metadata = {1: "One", 2: "Two"}

class ClientRequest(BaseModel):
    data: object



@router.get('/resources/{resource}')
async def get(resource: str):
    if resource == 'weathers' or resource == 'locations':
        res = db_queries.get_options(resource)
    else:
        res = "invalid resource type"

    return {"response": res}

@router.get('/getdate/')
async def get(weather: str, location: str):
    if weather != '' and location != '':
        res = db_queries.get_date(weather, location)
    else:
        res = "no query parametrs given"

    return {"response": res}


@router.get('/insource/{item_id}')
async def get(item_id: int):
    global caching_metadata
    print("get!")
    res = db_queries.get_number(item_id)
    print(res)
    return {"response": caching_metadata[item_id]}

@router.post('/insource/')
async def post(request: Request):
    global caching_metadata
    response = await request.json()   
    key = list(response.keys())[0]     
    val = response[key]
    db_queries.create_number(key, val)

    print(response)
    return response

@router.put('/insource/')
def put(data: ClientRequest):
    global caching_metadata
    # data.property = True   #changing some value
    #caching_metadata[data.id] = data
    return data


@router.patch('/insource/')
def patch(item_id: int, property, value):
    global caching_metadata
    # caching_metadata[item_id][property] = value
    # item = caching_metadata[item_id][property]
    # return item

@router.delete('/insource/{item_id}')
def delete(item_id):
    global caching_metadata
    item_id=int(item_id)
    item = caching_metadata[item_id]
    del caching_metadata[item_id]
    return item