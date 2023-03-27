from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class ChoiceModel(BaseModel):
    choice: str


class ItemModel(BaseModel):
    item: str

    @validator('item')
    def validate_choice(cls, item):
        if item not in ('rock', 'paper', 'scissors'):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="You have incorrect choice")
        return item
