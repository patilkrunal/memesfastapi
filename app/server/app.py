from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.meme import router as MemeRouter

app = FastAPI()
origins = [
    "https://gitkp11.github.io/memesfastapi/",
    "https://gitkp11.github.io/",
    "https://memefastapi.herokuapp.com/meme/",
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
