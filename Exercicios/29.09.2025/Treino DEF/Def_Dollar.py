def dolar_hoje():
    dolar = float(input('Digite a cotação do dolar hoje: '))
    return dolar

def seu_dinheiro():
    dinheiro = float(input('Digite quando você quer converter: '))
    return dinheiro

def cotacao():
    total_dolar = seu_dinheiro() / dolar_hoje()
    print(f'Você tem: {total_dolar:.2f}')

cotacao()