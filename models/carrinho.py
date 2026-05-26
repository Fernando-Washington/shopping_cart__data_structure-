from pydantic import BaseModel
from models.produto import Produto


class ItemCarrinho(BaseModel):
    produto: Produto
    quantidade: int