from pydantic import BaseSettings


class Settings(BaseSettings):
    DESCRIPTION: str = """This is me new game
    if you like interesting game with exciting story, come to me :) """
    VERSION: str = "0.1"
    CHOICE_LIST: list[str] = ("rock", "paper", "scissors")
    WIN_COMBINATIONS: tuple[tuple[str, ...], ...] = (
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    )
    LOSS_COMBINATIONS: tuple[tuple[str, ...], ...] = (
        ("rock", "paper"),
        ("paper", "scissors"),
        ("scissors", "rock"),
    )


config = Settings()
