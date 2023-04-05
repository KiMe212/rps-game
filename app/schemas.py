from fastapi import HTTPException, status
from pydantic import BaseModel, validator
from .settings import config


class ChoiceModel(BaseModel):
    your_choice: str
    pc_choice: str
    message: str


class ItemModel(BaseModel):
    item: str

    @validator("item")
    def validate_choice(cls, item):
        if item not in config.CHOICSE_LIST:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You have incorrect choice",
            )
        return item
