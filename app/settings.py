from pydantic import BaseSettings


class Settings(BaseSettings):
    DESCRIPTION: str = """This is me new game
    if you like interesting game with exciting story, come to me :) """
    VERSION: str = "0.1"
    CHOICE_LIST: list[str] = ("rock", "paper", "scissors")
    WIN_COMBINATIONS: dict[tuple[str, ...], str] = {
        ("rock", "scissors"): "You Win",
        ("paper", "rock"): "You Win",
        ("scissors", "paper"): "You Win",
    }
    LOSE_COMBINATIONS: dict[tuple[str, ...], str] = {
        ("rock", "paper"): "You Lose",
        ("paper", "scissors"): "You Lose",
        ("scissors", "rock"): "You Lose",
    }


config = Settings()
