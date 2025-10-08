lista = []
soma = 0
contagem = 0
cont = 0
while True:
    contagem += 1
    numero = int(input(f'Digite o {contagem}° Número:'))
    lista.append(numero)
    if numero == 0:
        break
    soma += numero
num = (contagem - 1)
print(f'A soma dos Números deu: {soma}\n'
      f'Você Digitou {num}° Números\n')

print('===X Números Digitados X===')
for i in lista:
    cont += 1
    print(f"{cont}° Número Digitado: {i}")