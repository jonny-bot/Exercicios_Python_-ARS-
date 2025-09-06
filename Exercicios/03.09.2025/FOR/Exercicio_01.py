# some os números de 1 até n (ex.: n=10 --> 55)

numero = int(input('Digite um Numero: '))

resultado = 0

for i in range(1, numero + 1):
    resultado = resultado + i
    print(f'{resultado}')