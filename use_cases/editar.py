from Mercado.use_cases.adicionar import gerarProduto
from Mercado.use_cases.buscar import buscarPorCodigo
from Mercado.repositorio import banco

def editarProduto(codigo, nome, categoria, preco):
    produto = buscarPorCodigo(codigo)
    if produto:
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco
        print('Dados alterados com Sucesso!')
    else:
        print('Produto não encontrado!')


