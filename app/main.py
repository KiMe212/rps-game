from fastapi import FastAPI

from app.routes import router

description = """
### This is relax game.

#### Here random, without negative)

You make choose and wait
"""


def init_routers(application: FastAPI):
    application.include_router(router)


def create_app():
    _app = FastAPI(
        title="Game of Rock Paper Scissors",
        description=description,
        version='0.1',
    )
    init_routers(_app)
    return _app


app = create_app()
