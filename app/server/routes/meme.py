from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_meme,
    delete_meme,
    retrieve_meme,
    retrieve_memes,
    update_meme,
)
 
from ..models.meme import (
    MemeSchema,
    UpdateMemeModel,
    ResponseModel,
    ErrorResponseModel,
)

router = APIRouter()


@router.post("/", response_description="meme data added into the database")
async def add_meme_data(meme: MemeSchema = Body(...)):
    meme = jsonable_encoder(meme)
    new_meme = await add_meme(meme)
    return ResponseModel(new_meme, "meme added successfully.")


@router.get("/", response_description="memes retrieved")
async def get_memes():
    memes = await retrieve_memes()
    if memes:
        return ResponseModel(memes, "memes data retrieved successfully")
    return ResponseModel(memes, "Empty list returned")


@router.get("/{id}", response_description="meme data retrieved")
async def get_meme_data(id):
    meme = await retrieve_meme(id)
    if meme:
        return ResponseModel(meme, "meme data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "meme doesn't exist.")


@router.put("/{id}")
async def update_meme_data(id: str, req: UpdateMemeModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_meme = await update_meme(id, req)
    if updated_meme:
        return ResponseModel(
            "meme with ID: {} name update is successful".format(id),
            "meme name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the meme data.",
    )


@router.delete("/{id}", response_description="meme data deleted from the database")
async def delete_meme_data(id: str):
    deleted_meme = await delete_meme(id)
    if deleted_meme:
        return ResponseModel(
            "meme with ID: {} removed".format(id), "meme deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "meme with id {0} doesn't exist".format(id)
    )
