from Mercado.use_cases.adicionar import gerarProduto
from Mercado.use_cases.buscar import buscarPorCodigo
from Mercado.use_cases.deletar import deletarProduto
from Mercado.use_cases.editar import editarProduto
from Mercado.use_cases.listar import listarProdutos

def menu():
    while True:
        print('=== BEM VINDO AO MENU ===')
        print('1 - Adicionar produto.')
        print('2 - Editar produto.')
        print('3 - Buscar produto.')
        print('4 - Deletar produto.')
        print('5 - Listar produto.')
        print('Outro - Sair.')
        opcao = int('Qual opção você deseja selecionar?')
        if opcao == 1:
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            gerarProduto(nome, categoria, preco)
        elif opcao == 2:
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            editarProduto(nome, categoria, preco)
        elif opcao == 3:
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            buscarPorCodigo(nome, categoria, preco)
        elif opcao == 4:
            codigo = int(input('Digite o nome do produto: '))
            deletarProduto(codigo)
        elif opcao == 5:
           listarProdutos()
        else:
            break



