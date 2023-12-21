from Mercado.repositorio import banco
from Mercado.use_cases.adicionar import gerarProduto
from Mercado.use_cases.buscar import buscarPorCodigo

def deletarProduto(codigo: int):
    produto = buscarPorCodigo(codigo)
    if produto:
        banco.remove(produto)
        print('produto removido com sucesso!')
    else:
        print('produto não encontrado!')

if __name__ -- '__main__':
    gerarProduto('mouse', 'perifericos', 199)
    print(banco)
    deletarProduto(1)
    print(banco)
    deletarProduto(1)