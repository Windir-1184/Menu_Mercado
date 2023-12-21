from Mercado.repositorio import banco
from Mercado.use_cases.adicionar import gerarProduto

def buscarPorCodigo(codigo: int) -> dict or None:
    for produto in banco:
        if codigo == produto['codigo']:
            return produto
    return None

if __name__ == "__main__":
    gerarProduto('mouse', 'periferico', 199)
    print(buscarPorCodigo(1))
    print(buscarPorCodigo(2))