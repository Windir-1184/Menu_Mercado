from Mercado.repositorio import banco

codigo = 0

def gerarProduto(nome, categoria, preco):
    global codigo
    codigo += 1
    produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "preco": preco
    }
    banco.append(produto)
    print('Produto adicionado com sucesso.')

if __name__ == "__main__":
    gerarProduto("mouse", "perifericos", 199)
    print(banco)