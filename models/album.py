from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel
from .publicacao import Publicacao
if TYPE_CHECKING:
    from .Perfil import Perfil, PerfilBase


class AlbumBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    capa: str


class Album(AlbumBase):
    perfil_id: int = Field(foreign_key='Perfil.id')
    perfil: 'Perfil' = Relationship(back_populates='albuns')
    pubs = list['Publicacao'] = Relationship(back_populates='albuns')


class AlbumbasePerfil(AlbumBase):
    perfil: 'PerfilBase'
