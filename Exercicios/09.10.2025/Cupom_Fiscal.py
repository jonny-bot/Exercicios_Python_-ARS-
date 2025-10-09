soma = 0
contagem = 1
registrados = []

while True:
    numero = int(input(f"Digite o {contagem}° Número: "))
    if numero == 0:
        break
    registrados.append(numero)
    soma += numero
    contagem += 1

print(f'\nA soma dos Números deu: {soma}')
print(f'Você digitou {contagem - 1} Números.\n')

contagem_numeros = 1
for i in registrados:
    print(f'O {contagem_numeros}° número digitado: {i}')
    contagem_numeros += 1
