import pytest

from app.services import get_message_from_game_result


@pytest.mark.parametrize(
    "you_choice, pc_choice, message",
    [
        ("paper", "rock", "You Win"),
        ("scissors", "rock", "You Lose"),
        ("rock", "rock", "Tie"),
    ],
)
def test_get_message_from_game_result(you_choice, pc_choice, message):
    assert get_message_from_game_result(you_choice, pc_choice) == message
