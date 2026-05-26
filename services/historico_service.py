from models.historico import Compra
from structures.lista_encadeada import ListaEncadeada

historico_compras = ListaEncadeada()


def salvar_compra(compra: Compra):
    historico_compras.adicionar(compra)


def listar_historico():
    return historico_compras.listar()