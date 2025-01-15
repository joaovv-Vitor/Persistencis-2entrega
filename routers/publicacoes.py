
from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models.publicacao import Publicacao

router = APIRouter(
    prefix='/publicacoes',  # prefixo dos endpoints de publicações
    tags=['Publicacoes'],  # tag que agrupa na documentação automática
)


@router.post('/new_pub', response_model=Publicacao)
def create_pub(pub: Publicacao, secao: Session = Depends(get_session)):
    secao.add(pub)
    secao.commit()
    secao.refresh(pub)
    return pub
