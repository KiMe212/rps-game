import pytest

from app.schemas import GameResult
from app.services import get_message_from_game_result


@pytest.mark.parametrize(
    "result, message",
    [
        (GameResult.WIN, "You Win"),
        (GameResult.LOSS, "You Lose"),
        (GameResult.TIE, "Tie"),
    ],
)
def test_get_message_from_game_result(result, message):
    assert get_message_from_game_result(result) == message
