def entrada():
    numero = int(input('Digite a tabuada: '))
    return numero

def tabuada():
    entra = entrada()
    for i in range(1, 10 + 1):
        print(f'{entra} x {i} = {entra * i}')

tabuada()