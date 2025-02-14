from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

if TYPE_CHECKING:
    from .Perfil import Perfil, PerfilBase
    from .album import Album, AlbumbasePerfil
    # from .pubAlbum import PubAlbum


class PubAlbum(SQLModel, table=True):
    id_pub: int = Field(default=None, foreign_key='Publicacao.id',
                        primary_key=True)
    id_album: int = Field(default=None, foreign_key='Album.id',
                          primary_key=True)

    __table_args__ = (
        UniqueConstraint('id_pub', 'id_album'),
    )


class PubBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    legenda: str | None = Field(default=None)
    curtidas: int = Field(default=0)
    data_criacao: datetime = Field(default_factory=lambda:
                               datetime.now(timezone.utc))
    caminho_imagem: str


class Publicacao(PubBase, table=True):
    user_id: int = Field(foreign_key='Perfil.id')
    user: 'Perfil' = Relationship(back_populates='pubs')
    albuns: list['Album'] = Relationship(link_model=PubAlbum, back_populates='pubs')


class PubCompleta(PubBase):
    user: 'PerfilBase' = None
    albuns: list['AlbumbasePerfil'] = None
