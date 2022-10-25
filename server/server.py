# for convience, run this script to create a db and tables:
#       Database.dbInitializer
# note: run it only once :)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from Routes import externalRouts
from Routes import internalRouts

app = FastAPI()

app.include_router(externalRouts.router)
app.include_router(internalRouts.router)

app.mount('/', StaticFiles(directory='..\client', html = True), name='client')

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)