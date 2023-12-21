from Mercado.repositorio import banco
from Mercado.use_cases.adicionar import gerarProduto

def listarProdutos():
    print('--- LISTA DE PRODUTOS ---')
    for produto in banco:
        print(f"Codigo: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}]")

if __name__ == "__main__":
    gerarProduto('mouse', 'periferico', 155)
    gerarProduto('mousepad', 'acessorios', 80)
    listarProdutos()