from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.meme import router as MemeRouter

app = FastAPI()
origins = [
    "https://diwakarsingh18277.github.io",
    "https://gitkp11.github.io",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(MemeRouter, tags=["Meme"], prefix="/memes")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
