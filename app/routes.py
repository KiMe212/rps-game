import random

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.schemas import ChoiceModel, ItemModel
from app.services import CHOICE_LIST, get_winner

router = APIRouter(
    prefix="/rps",
    tags=['router'],
)


@router.post("/rps", status_code=status.HTTP_200_OK)
def play_rps(choice_model: ChoiceModel):
    choice_pc = random.choice(CHOICE_LIST)
    validated_choice = ItemModel(item=choice_model.choice)
    winner = get_winner(choice_first=choice_model.choice,
                        choice_second=choice_pc)
    return JSONResponse(content={
        'choice': choice_model.choice,
        'winner': winner
    },
        status_code=status.HTTP_200_OK)


@router.get('/rps', status_code=status.HTTP_200_OK)
def play_rps(choice: str):
    choice_pc = random.choice(CHOICE_LIST)
    validated_choice = ItemModel(item=choice)
    winner = get_winner(choice_first=choice, choice_second=choice_pc)
    return JSONResponse(content={
        'choice': choice,
        'winner': winner
    },
        status_code=status.HTTP_200_OK)
