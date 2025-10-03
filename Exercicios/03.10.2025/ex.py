soma = 0
num = 1
while True:
    numero = int(input(f"Digite o {num}° Número (0 para parar): "))
    num += 1
    if numero == 0:
        break
    soma += numero
num = (num - 2)
if num == 1:
    print(f"A soma dos Números digitados é: {soma}\n"
          f"Você Digitou {num} Número.")
else:
    print(f"A soma dos Números digitados é: {soma}\n"
          f"Você Digitou {num} Números.")