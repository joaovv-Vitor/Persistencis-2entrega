import logging
import os

from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

# carregar as variaveis do arquivo .env
load_dotenv()

# configurar o logger p obter informações da rodagem
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# obter a url do banco
DATABASE_URL = os.getenv('DATABASE_URL')

# criar a conexao com o banco
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
