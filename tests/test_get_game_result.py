import pytest

from app.schemas import GameResult
from app.services import get_game_result


@pytest.mark.parametrize(
    "you_choice, pc_choice, message",
    [
        ("paper", "rock", GameResult.WIN),
        ("scissors", "rock", GameResult.LOSS),
        ("rock", "rock", GameResult.TIE),
    ],
)
def test_get_game_result(you_choice, pc_choice, message):
    assert get_game_result(you_choice, pc_choice) == message
