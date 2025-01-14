from sqlmodel  import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .album import Album, albumbasePerfil
    from .publicacao import Publicacao


class PerfilBase(SQLModel):
    id: int | None = Field(default = None, primary_key = True)
    email: str = Field(unique = True)
    nome: str
    bio: str
    
class perfil(PerfilBase, table = True):
    albuns: list['Album'] = Relationship(back_populates='perfil')
    Publicacao: list['Publicacao'] = Relationship(back_populates='perfil')


class perfilBaseAlbumPublicao(PerfilBase):
    perfil: PerfilBase | None
    album: list[albumbasePerfil] = None

