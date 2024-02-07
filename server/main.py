
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import httpx

import os
from dotenv import load_dotenv

from consts import LOCATION


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# create a global client
client = httpx.AsyncClient()

async def call_api(url: str):

  r = await client.get(url)
  return r



load_dotenv()
SECRET_KEY = os.getenv("OPENWEATHERMAP_KEY")
print(SECRET_KEY)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/location/{name}")
async def read_item(name: str):
    if LOCATION.get(name) is not None:
      url=f"https://api.openweathermap.org/data/2.5/weather?lat={LOCATION[name][0]}&lon={LOCATION[name][1]}&appid={SECRET_KEY}&units=metric"
      results = await call_api(url)
      return results.json()
    else: 
      return 'wrong location'