from enum import Enum

from app.settings import config


class GameResult(Enum):
    WIN = "Win"
    LOSS = "Lose"
    TIE = "Tie"


def get_game_result(first_choice, second_choice):
    if (first_choice, second_choice) in list(config.WIN_COMBINATIONS.keys()):
        return GameResult.WIN.value
    elif (first_choice, second_choice) in list(config.LOSE_COMBINATIONS.keys()):
        return GameResult.LOSS.value
    else:
        return GameResult.TIE.value


def get_message_from_game_result(first_choice, second_choice):
    game_result = get_game_result(first_choice, second_choice)
    game_tuple = (first_choice, second_choice)
    if game_result == "Win":
        return config.WIN_COMBINATIONS[game_tuple]
    elif game_result == "Lose":
        return config.LOSE_COMBINATIONS[game_tuple]
    elif game_result == "Tie":
        return "Tie"
