soma = 0
contador = 0

while True:
    numero = int(input(f'Digite {contador + 1}° número: '))
    if numero == 0:
        break
    soma += numero
    contador += 1

if contador > 0:
    print(f'A Média dos Números deu: {soma / contador}')
