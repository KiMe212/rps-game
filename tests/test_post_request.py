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
def test_post_choice(choice, answer, test_client):
    response = test_client.post("/game/rps", json={"choice": choice})

    assert response.status_code == 200
    assert response.json() == {
        "your_choice": choice,
        "pc_choice": "paper",
        "message": answer,
    }


def test_validate_post_choice(test_client):
    response = test_client.post("/game/rps", json={"choice": "234342"})

    assert response.status_code == 400
    assert response.json() == {"detail": "You have incorrect choice"}
