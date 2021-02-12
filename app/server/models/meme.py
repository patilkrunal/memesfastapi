from typing import Optional
from pydantic import BaseModel, Field


class MemeSchema(BaseModel):
    user: str = Field(...)
    url: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "user": "John Doe",
                "url": "http://localhost:8000/docs#/"
            }
        }


class UpdateMemeModel(BaseModel):
    user: Optional[str]
    url: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "user": "John Doe",
                "url": "http://localhost:8000/docs#/"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
