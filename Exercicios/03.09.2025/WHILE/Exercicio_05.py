numero = int(input("Digite um número inteiro não negativo: "))

fatorial = 0
contador = numero

if numero < 0:
    print("O fatorial não é definido para números negativos.")

elif numero == 0 or numero == 1:
    fatorial = 1

else:
    while contador > 1:
        fatorial *= contador
        contador -= 1

print(f"O fatorial de {numero} é {fatorial}")