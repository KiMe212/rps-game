from pydantic import BaseSettings


class Settings(BaseSettings):
    DESCRIPTION: str = "None"
    VERSION: int = 0.1
    CHOICSE_LIST: list = ("rock", "paper", "scissors")
    WIN_AND_LOSE_COMBINATIONS: dict = {
        ("rock", "scissors"): "You Win",
        ("paper", "rock"): "You Win",
        ("scissors", "paper"): "You Win",
        ("rock", "paper"): "You Lose",
        ("paper", "scissors"): "You Lose",
        ("scissors", "rock"): "You Lose",
    }

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
