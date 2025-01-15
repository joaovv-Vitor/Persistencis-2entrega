# from http import HTTPStatus

# from fastapi import FastAPI

# app = FastAPI()


# @app.get('/', status_code=HTTPStatus.OK)
# def read_root():
#     return {'message': 'olar mundo!!'}

from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_db_and_tables
from routers import publicacoes


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(publicacoes.router)
