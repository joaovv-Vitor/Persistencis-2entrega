from sqlmodel  import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .albuns import Albuns
    from .publicacoes import Publicacao


class PerfilBase(SQLModel):
    id: int | None = Field(default = None, primary_key = True)
    email: str = Field(unique = True)
    nome: str
    bio: str
    

