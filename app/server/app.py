from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.meme import router as MemeRouter

app = FastAPI()
origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8000",
    # "http://localhost:5500",
    "https://memefastapi.herokuapp.com/meme/",
    "https://gitkp11.github.io/memesfastapi/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(MemeRouter, tags=["Meme"], prefix="/meme")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
