from typing import Optional
from pydantic import BaseModel, Field


class MemeSchema(BaseModel):
    user: str = Field(...)
    url: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "user": "Diwakar Singh",
                "url": "http://www.quickmeme.com/img/5d/5d1e705c13192f4cafed66b6c91c6c0bea852181393fed347615c448ac0993d1.jpg"
            }
        }


class UpdateMemeModel(BaseModel):
    user: Optional[str]
    url: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "user": "Diwakar Singh",
                "url": "http://www.quickmeme.com/img/5d/5d1e705c13192f4cafed66b6c91c6c0bea852181393fed347615c448ac0993d1.jpg"
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
