from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@patch('random.choice', lambda x: 'paper')
@pytest.mark.parametrize(
    'choices, answer',
    [
        ('paper', 'Draw'),
        ('scissors', 'You Win, i have paper'),
        ('rock', 'You Lose, i have paper')
    ]
)
def test_get_choice(choices, answer):
    response = client.get('/rps/rps', params={'choice': choices})
    assert response.status_code == 200
    assert response.json() == {"choice": choices, "winner": answer}


def test_validate_get_choice():
    response = client.get('/rps/rps', params={'choice': '32ws43'})
    assert response.status_code == 400
    assert response.json() == {'detail': "You have incorrect choice"}


@patch('random.choice', lambda x: 'paper')
@pytest.mark.parametrize(
    'choices, answer',
    [
        ('paper', 'Draw'),
        ('scissors', 'You Win, i have paper'),
        ('rock', 'You Lose, i have paper')
    ]
)
def test_post_choice(choices, answer):
    response = client.post('/rps/rps', json={'choice': choices})
    assert response.status_code == 200
    assert response.json() == {"choice": choices, "winner": answer}


def test_validate_post_choice():
    response = client.post('/rps/rps', json={'choice': 234342})
    assert response.status_code == 400
    assert response.json() == {'detail': "You have incorrect choice"}
