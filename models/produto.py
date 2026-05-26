from pydantic import BaseModel

class Produto(BaseModel):
    codigo: int
    nome: str
    preco: float
    quantidade_estoque: int
    categoria: str