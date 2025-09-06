# imprima a tabuada do num de 1 a 10.

tabuada = int(input('Tabuada: \n'))

for var in range(1, 11):
    resultado = var * tabuada
    print(f'{tabuada} * {var} = {resultado}')
