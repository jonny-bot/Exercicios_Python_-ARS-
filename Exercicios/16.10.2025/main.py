soma = 0
contagem = 0
lista = []
while True:
    try:
        contagem += 1
        numero = int(input(f'Digite o {contagem}° Número: '))
        if numero == 0:
            break
        soma += numero
        lista.append(numero)
    except ValueError:
        print('Digite uma entrada válida')
print(f'A soma dos Números deu: {soma}')

cont = 0
for i in lista:
    cont += 1
    print(f'O {cont}° Número Digitado: {i}')