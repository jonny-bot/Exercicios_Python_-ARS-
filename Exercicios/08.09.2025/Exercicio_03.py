numeros = [] 
soma = 0
pares = 0
impares = 0
menor = float('inf')
maior = float('-inf')

while True:
    entrada = input("Digite um número ou 'fim' para terminar: ")
    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        numeros.append(numero)

        soma += numero
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

    except ValueError:
        print("Entrada inválida. Por favor, insira um número ou 'fim'.")

if numeros:
    media = soma / len(numeros)
    total_valores = len(numeros)

    print("\n--- Resultados ---")
    print(f"Total de valores inseridos: {total_valores}")
    print(f"Soma dos valores: {soma}")
    print(f"Média dos valores: {media:.2f}")
    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")
else:
    print("\nNão foram inseridos números para calcular.")
