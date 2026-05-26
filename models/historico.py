from pydantic import BaseModel
from models.carrinho import ItemCarrinho


class Compra(BaseModel):
    itens: list[ItemCarrinho]
    total: float