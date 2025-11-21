resultado = 1
numero = int(input('Digite a contagem até: '))
for i in range(1, numero + 1):
    resultado *= i
print(f'Resultado: {resultado}')
