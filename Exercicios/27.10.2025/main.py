soma = 0
contagem = 1
lista = []
while True:
    try:
        numero = int(input(f'Digite o {contagem}° Número: '))
        lista.append(numero)
        if numero == 0:
            break
        soma += numero
        contagem += 1
    except ValueError:
        print('Digite uma entrada Válida!!!')
print(f'A soma dos números deu: {soma}\n'
      f'Você digitou: {contagem - 1} Números')

for i in lista:
    if i != 0:
        print(i)