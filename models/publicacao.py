from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime 
from models import Usuario, AlbumPub
from typing import List

class Publicacao(SQLModel, table= True):
    __tablename__= 'Publicacoes'
    id_pub: int | None = Field(default=None, primary_key=True)
    id_autor: int | None = Field(foreign_key="usuario.id_user")
    legenda: str | None = Field(default=None)
    likes: int = Field(default=0)
    id_autor: int 
    caminho_imagem: str
    data_criacao: datetime
    
    autor: Usuario = Relationship(back_populates='Publicacao')
    albuns: List['AlbumPub'] = Relationship(back_populates='Publicacao')