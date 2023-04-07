import random

from fastapi import APIRouter, status

from app.schemas import ChoiceModel, ItemModel
from app.services import get_message_from_game_result
from app.settings import config

router = APIRouter(
    prefix="/game",
    tags=["router"],
)


@router.post(
    "/rps",
    status_code=status.HTTP_200_OK,
    response_model=ChoiceModel,
)
def play_rps(choice_model: ChoiceModel):
    pc_choice = random.choice(config.CHOICE_LIST)
    validated_choice = ItemModel(item=choice_model.your_choice)
    winner = get_message_from_game_result(
        first_choice=validated_choice.item,
        second_choice=pc_choice,
    )
    return ChoiceModel(
        your_choice=validated_choice.item,
        pc_choice=pc_choice,
        message=winner,
    )


@router.get(
    "/rps",
    status_code=status.HTTP_200_OK,
    response_model=ChoiceModel,
)
def play_game_rps(choice: str):
    pc_choice = random.choice(config.CHOICE_LIST)
    validated_choice = ItemModel(item=choice)
    winner = get_message_from_game_result(
        first_choice=validated_choice.item,
        second_choice=pc_choice,
    )
    return {
        "your_choice": validated_choice.item,
        "pc_choice": pc_choice,
        "message": winner,
    }
