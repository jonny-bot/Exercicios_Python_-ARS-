def gerar_lista():
    lista = list(range(10))
    return lista

def analisar_numero(numero):
    if numero in gerar_lista():
        print('O Número Consta na Lista!')
    else:
        print('O Número Não Consta na Lista!')

numero = int(input('Digite um Número: '))

analisar_numero(numero)
