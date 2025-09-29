def verificardor(numero):
    return numero % 2 == 0

def entrada_numero():
    numero = int(input('Digite um Número: '))
    return numero

def verificador(numero):
    if verificardor(numero):
        print('O Número é PAR!!!')
    else:
        print('O Número é ÍMPAR!!!')

# Execução
numero_digitado = entrada_numero()
verificador(numero_digitado)