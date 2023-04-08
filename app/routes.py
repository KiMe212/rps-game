import random

from fastapi import APIRouter, status

from app.schemas import ChoiceModel, ChoiceResponseModel, ItemModel
from app.services import get_game_result, get_message_from_game_result
from app.settings import config

router = APIRouter(
    prefix="/game",
    tags=["router"],
)


@router.post(
    "/rps",
    status_code=status.HTTP_200_OK,
    response_model=ChoiceResponseModel,
)
def play_rps(choice_model: ChoiceModel):
    pc_choice = random.choice(config.CHOICE_LIST)
    validated_choice = ItemModel(item=choice_model.your_choice)
    game_result = get_game_result(
        first_choice=choice_model.your_choice,
        second_choice=pc_choice,
    )
    message = get_message_from_game_result(result=game_result)
    return ChoiceResponseModel(
        your_choice=validated_choice.item,
        pc_choice=pc_choice,
        message=message,
    )


@router.get(
    "/rps",
    status_code=status.HTTP_200_OK,
    response_model=ChoiceResponseModel,
)
def play_game_rps(choice: str):
    pc_choice = random.choice(config.CHOICE_LIST)
    validated_choice = ItemModel(item=choice)
    game_result = get_game_result(
        first_choice=choice,
        second_choice=pc_choice,
    )
    message = get_message_from_game_result(result=game_result)
    return ChoiceResponseModel(
        your_choice=validated_choice.item,
        pc_choice=pc_choice,
        message=message,
    )
