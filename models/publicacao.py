from sqlmodel import SQLModel, Field

class Publicacao(SQLModel, table= True):
    __tablename__= 'Publicacoes'
    id_pub: int = Field(default=None, primary_key=True)
    legenda: str | None = Field(default=None)
    likes: int
    id_autor: int 