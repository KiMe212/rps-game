## Manual of game

___

1. #### Install Poetry

* *Linux, macOS, Windows (WSL)*

`curl -sSL https://install.python-poetry.org | python3 -`

* *Windows (Powershell)*

`(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`

2. #### Settings virtual
curl -sSL https://install.python-poetry.org | python3 -

#### In the root folder
poetry install   
poetry run uvicorn app.main:app --reload



