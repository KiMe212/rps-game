from unittest.mock import patch

import pytest


@patch("random.choice", lambda x: "paper")
@pytest.mark.parametrize(
    "choice, answer",
    [
        ("paper", "Tie"),
        ("scissors", "You Win"),
        ("rock", "You Lose"),
    ],
)
def test_get_choice(choice, answer, test_client):
    response = test_client.get("/game/rps", params={"choice": choice})

    assert response.status_code == 200
    assert response.json() == {
        "your_choice": choice,
        "pc_choice": "paper",
        "message": answer,
    }


def test_validate_get_choice(test_client):
    response = test_client.get("/game/rps", params={"choice": "32ws43"})

    assert response.status_code == 400
    assert response.json() == {"detail": "You have incorrect choice"}
