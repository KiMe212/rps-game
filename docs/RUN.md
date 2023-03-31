## Manual of game

___

1. #### Install Poetry

* *Linux, macOS, Windows (WSL)*

`curl -sSL https://install.python-poetry.org | python3 -`

* *Windows (Powershell)*

`(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`

2. #### Settings virtual

* `poetry init`
* `poetry shell`
* *settings -> Project: rps-game -> Python Interpreter -> Add Interpreter -> Add Local Interpreter -> Existing ->Add Python file*

    Path ``C:\Users\AppData\Local\pypoetry\Cache\virtualenvs\(your project)\Scripts\python``

    -> Apply
* `poetry add fastapi uvicorn pytest `

3. #### Start projects

`uvicorn app.main:app --reload`



