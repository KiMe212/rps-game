from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@patch("random.choice", lambda x: "paper")
@pytest.mark.parametrize(
    "choices, answer",
    [("paper", "Draw"), ("scissors", "You Win"), ("rock", "You Lose")],
)
def test_post_choice(choices, answer):
    response = client.post("/game/rps", params={"choice": choices})
    assert response.status_code == 200
    assert response.json() == {
        "your_choice": choices,
        "pc_choice": "paper",
        "message": answer,
    }


def test_validate_post_choice():
    response = client.post("/game/rps", json={"choice": "234342"})
    assert response.status_code == 400
    assert response.json() == {"detail": "You have incorrect choice"}
