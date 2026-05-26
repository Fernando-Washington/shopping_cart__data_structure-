from models.carrinho import ItemCarrinho
from structures.pilha import Pilha

carrinho = []
historico_acoes = Pilha()


def adicionar_item(item: ItemCarrinho):
    carrinho.append(item)

    historico_acoes.empilhar({
        "acao": "adicionar",
        "item": item
    })

    return item


def remover_item(codigo_produto: int):
    for item in carrinho:
        if item.produto.codigo == codigo_produto:
            carrinho.remove(item)

            historico_acoes.empilhar({
                "acao": "remover",
                "item": item
            })

            return item

    return None


def listar_carrinho():
    return carrinho


def calcular_total():
    total = 0

    for item in carrinho:
        total += item.produto.preco * item.quantidade

    return total


def desfazer_ultima_acao():
    if historico_acoes.esta_vazia():
        return "Nenhuma ação para desfazer"

    ultima_acao = historico_acoes.desempilhar()

    item = ultima_acao["item"]

    if ultima_acao["acao"] == "adicionar":
        if item in carrinho:
            carrinho.remove(item)

    elif ultima_acao["acao"] == "remover":
        carrinho.append(item)

    return "Última ação desfeita"