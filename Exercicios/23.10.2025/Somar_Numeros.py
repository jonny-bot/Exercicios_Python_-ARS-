soma = 0
contagem = 0
lista = []
while True:
    try:
        contagem += 1
        numero = int(input(f"Digite o {contagem}° Número: "))
        lista.append(numero)
        if numero == 0:
            break
        soma += numero
        lista2 = [x for x in lista if x != 0]
    except ValueError:
        print('Digite Uma Entrada Válida!!!')
        contagem -= 1
print(f'A soma dos Números deu: {soma}\n'
      f'O maior Número Digitado é o: {max(lista2)}\n'
      f'O menor Número Digitado é o: {min(lista2)}')