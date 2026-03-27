def calcular_imposto(valor):

    match case:

        case valor if valor <= 1000:
            imposto = valor + (valor * 0.1)

        case valor if valor <= 5000:
            imposto = valor + (valor * 0.2)

        case _:
            imposto = valor + (valor * 0.4)

    return imposto



valor = float(input("Digite o valor: "))
imposto_calculado = calcular_imposto(valor)

print(f"O imposto calculado é: {imposto_calculado:.2f}")