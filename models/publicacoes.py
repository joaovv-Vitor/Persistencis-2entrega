from datetime import datetime, timezone
from typing import List

from sqlmodel import Field, Relationship, SQLModel

from .albuns import Album
from .perfis import Perfil


class PubAlbum(SQLModel, table=True):
    id_pub: int = Field(default=None,
                         foreign_key='Publicacao.id', primary_key=True)
    id_album: int = Field(default=None,
                          foreign_key='Album.id', primary_key=True)


class PubBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    legenda: str | None = Field(default=None)
    curtidas: int = Field(default=0)
    data_criacao: datetime = Field(default_factory=lambda:
                               datetime.now(timezone.utc))
    caminho_imagem: str


class Publicacao(PubBase, table=True):
    user_id: int = Field(foreign_key='perfil.id')
    user: Perfil = Relationship(back_populates='pubs')
    albuns: List[Album] = Relationship(link_model=PubAlbum)


class PubCompleta(PubBase):
    user: Perfil | None
    albuns: List[Album] | None
