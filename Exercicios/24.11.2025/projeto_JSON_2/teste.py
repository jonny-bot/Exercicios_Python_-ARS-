'''
num = 1
soma = 0
while True:
    numero = int(input(f'Digite o {num}° Número: '))
    num += 1
    if numero == 0:
        break
    soma += numero
print(f'A Soma deu: {soma}\n'
      f'Você Digitou {num - 2} Número(s).')
'''

while True:
    try:
        resposta_correta = int(input("Digite um número inteiro entre 1 e 4: "))
        if resposta_correta in (1, 2, 3, 4):
            print(f"Você digitou um número válido: {resposta_correta}")
            break  # Sai do loop se a entrada for válida
        else:
            print(f"Você digitou: {resposta_correta}, que não está entre 1 e 4. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

