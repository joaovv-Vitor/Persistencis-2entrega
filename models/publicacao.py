from datetime import datetime
from typing import List

from sqlmodel import Field, Relationship, SQLModel

from models import AlbumPub, Usuario


class Publicacao(SQLModel, table=True):
    __tablename__ = 'Publicacoes'
    id_pub: int | None = Field(default=None, primary_key=True)
    id_autor: int | None = Field(foreign_key="usuario.id_user")
    legenda: str | None = Field(default=None)
    likes: int = Field(default=0)
    caminho_imagem: str
    data_criacao: datetime = Field(default_factory=lambda: datetime.now())

    autor: Usuario = Relationship(back_populates='Publicacao')
    albuns: List['AlbumPub'] = Relationship(back_populates='Publicacao')
