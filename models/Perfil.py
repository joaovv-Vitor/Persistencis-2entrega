from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

if TYPE_CHECKING:
    from .album import Album, AlbumbasePerfil
    from .publicacao import Publicacao

class PerfilBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    nome: str
    bio: str
    __table_args__ = (UniqueConstraint('email'),)


class Perfil(PerfilBase, table=True):
    albuns: list['Album'] = Relationship(back_populates='perfil')
    pubs: list['Publicacao'] = Relationship(back_populates='user')


class PerfilBaseAlbumPublicao(PerfilBase):
    perfil: PerfilBase = None
    albuns: list['AlbumbasePerfil'] = None
