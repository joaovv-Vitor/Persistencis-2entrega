from sqlmodel import Field, SQLModel, UniqueConstraint


class PubAlbum(SQLModel, table=True):
    id_pub: int = Field(default=None, foreign_key='Publicacao.id',
                        primary_key=True)
    id_album: int = Field(default=None, foreign_key='Album.id',
                          primary_key=True)

    __table_args__ = (
        UniqueConstraint('id_pub', 'id_album'),
    )
