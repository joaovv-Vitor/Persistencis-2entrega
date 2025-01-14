from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .Perfil import Perfil, PerfilBase


class AlbumBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    capa: str


class album(AlbumBase):
    perfil_id: int = Field(foreign_key='user.id')
    perfil: 'Perfil' = Relationship(back_populates='albuns')


class albumbasePerfil(AlbumBase):
    perfil: PerfilBase
