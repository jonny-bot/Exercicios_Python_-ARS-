def calcular_notas(saque):
    notas = [100, 50, 20, 10, 5]
    resultado = {}

    for nota in notas:
        quantidade = saque // nota
        if quantidade > 0:
            resultado[nota] = quantidade
            saque -= quantidade * nota

    return resultado


saque = int(input("Digite o valor: "))
notas_retiradas = calcular_notas(saque)

print("Notas retiradas:")
for nota, quantidade in notas_retiradas.items():
    print(f"{quantidade} nota(s) de R$ {nota}")