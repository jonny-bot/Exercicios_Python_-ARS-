soma_total = 0

desconto = 5

while True:

    preco = input("Digite um número (ou 0 para terminar): ")

    try:
        numero = int(preco)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        continue

    if numero == 0:
        break

    soma_total += numero

if soma_total >= 100:
    print(f'O preço total com desconto fica: {soma_total - (soma_total * (desconto / 100))}')
else:
    print(f"A soma total dos números digitados é: {soma_total}")