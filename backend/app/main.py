from fastapi import (
    FastAPI,
    Body,
    Response,
)
from fastapi.middleware.cors import CORSMiddleware
from db.base import database

import base64
from PIL import Image
from io import BytesIO
import time

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/", status_code=200)
async def test(req = Body(...)):
    # print(type(req))
    # print(req[0:10])
    start = time.time()
    name = "alex"
    im = Image.open(BytesIO(base64.b64decode(req)))
    im.save(f'photo/{name}_{str(int(time.time()))}.png', 'PNG')
    return Response(status_code=200, content="ok")