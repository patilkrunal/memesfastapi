from typing import Optional
from pydantic import BaseModel, Field


class MemeSchema(BaseModel):
    name: str = Field(...)
    url: str = Field(...)
    caption: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Diwakar Singh",
                "url": "https://www.exterro.com/images/uploads/blogPosts/Monkey-Puppet-Meme-LinkedIn.png",
                "caption": "This is a meme"
            }
        }


class UpdateMemeModel(BaseModel):
    name: Optional[str]
    url: Optional[str]
    caption: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Diwakar Singh",
                "url": "https://www.exterro.com/images/uploads/blogPosts/Monkey-Puppet-Meme-LinkedIn.png",
                "caption": "This is a meme"
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
