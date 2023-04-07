import pytest

from app.services import get_game_result


@pytest.mark.parametrize(
    "you_choice, pc_choice, message",
    [
        ("paper", "rock", "Win"),
        ("scissors", "rock", "Lose"),
        ("rock", "rock", "Tie"),
    ],
)
def test_get_game_result(you_choice, pc_choice, message):
    assert get_game_result(you_choice, pc_choice) == message
