from fastapi import FastAPI
from .routes.meme import router as MemeRouter

app = FastAPI()

app.include_router(MemeRouter, tags=["Meme"], prefix="/meme")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
