from fastapi import FastAPI

from app.routes import router
from app.settings import config

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
        description=config.DESCRIPTION,
        version=config.VERSION,
    )
    init_routers(_app)
    return _app


app = create_app()
