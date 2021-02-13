import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config
import urllib.parse

# MongoDB attributes
mongodb_uri = 'mongodb+srv://memestore:Admin_11@cluster0.ypreh.mongodb.net/memestore_db-atlas?retryWrites=true&w=majority'
client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_uri)
database = client.memes_db
meme_collection = database.get_collection("meme_collection")


def meme_helper(meme) -> dict:
    return {
        "id": str(meme["_id"]),
        "user": meme["user"],
        "url": meme["url"],
    }


async def retrieve_memes():
    memes = []
    async for meme in meme_collection.find().sort([('$natural', -1)]):
        memes.append(meme_helper(meme))
    return memes


async def add_meme(meme_data: dict) -> dict:
    meme = await meme_collection.insert_one(meme_data)
    new_meme = await meme_collection.find_one({"_id": meme.inserted_id})
    return meme_helper(new_meme)


async def retrieve_meme(id: str) -> dict:
    meme = await meme_collection.find_one({"_id": ObjectId(id)})
    if meme:
        return meme_helper(meme)


async def update_meme(id: str, data: dict):
    if len(data) < 1:
        return False
    meme = await meme_collection.find_one({"_id": ObjectId(id)})
    if meme:
        updated_meme = await meme_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_meme:
            return True
        return False


async def delete_meme(id: str):
    meme = await meme_collection.find_one({"_id": ObjectId(id)})
    if meme:
        await meme_collection.delete_one({"_id": ObjectId(id)})
        return True
