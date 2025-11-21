def calcular_taxa(preco):

    preco = float(preco)

    if preco < 1000:
        preco = preco + (preco * 0.1)
        print(f'O preço final fica: {preco}')

    elif preco < 2000:
        preco = preco + (preco * 0.2)
        print(f'O preço final fica: {preco}')

    elif preco < 3000:
        preco = preco + (preco * 0.3)
        print(f'O preço final fica: {preco}')

    else:
        preco = preco + (preco * 0.40)
        print(f'O preço final fica: {preco}')

    return preco


preco = float(input('Digite o Valor do produto: '))

preco_final = calcular_taxa(preco)
