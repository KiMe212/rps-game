from app.services import get_message_from_game_result


def test_get_message_from_game_result():
    assert get_message_from_game_result("paper", "rock") == "You Win"
    assert get_message_from_game_result("scissors", "rock") == "You Lose"
    assert get_message_from_game_result("paper", "paper") == "Draw"
