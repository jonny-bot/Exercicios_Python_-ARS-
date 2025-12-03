soma = 0
contador = 0
while True:

    try:

        numero = int(input(f'Digite a {contador + 1}° Idade: '))
        contador += 1

        if numero == 0:
            break
        soma += numero

    except ValueError:
        print('Digite uma Entrada Válida!')

print(f'A soma das Idades deu: {soma}\n'
      f'A Média das Idades deu: {int((soma / (contador - 1)))}')
