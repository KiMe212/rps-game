from app.schemas import GameResult
from app.settings import config


def get_game_result(first_choice, second_choice):
    game_tuple = (first_choice, second_choice)
    if game_tuple in config.WIN_COMBINATIONS:
        return GameResult.WIN
    elif game_tuple in config.LOSE_COMBINATIONS:
        return GameResult.LOSS
    else:
        return GameResult.TIE


def get_message_from_game_result(result):
    return result.value
