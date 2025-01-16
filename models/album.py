from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .Perfil import Perfil, PerfilBase
    from .publicacao import Publicacao
    from .pubAlbum import PubAlbum


class AlbumBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    capa: str


class Album(AlbumBase):
    perfil_id: int = Field(foreign_key='Perfil.id')
    perfil: 'Perfil' = Relationship(back_populates='albuns')
    pubs = list['Publicacao'] = Relationship(link_model=PubAlbum, back_populates="albuns")


class AlbumbasePerfil(AlbumBase):
    perfil: 'PerfilBase'
