import logging
import os
import sqlite3

from dotenv import load_dotenv
from sqlalchemy import Engine, event
from sqlmodel import Session, SQLModel, create_engine

# carregar as variaveis do arquivo .env
load_dotenv()

# configurar o logger p obter informações da rodagem
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# obter a url do banco
# criar a conexao com o banco
engine = create_engine(os.getenv('DATABASE_URL'))


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
    logging.info("Tabelas criadas!")


def get_session() -> Session:
    return Session(engine)


@event.listens_for(Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
