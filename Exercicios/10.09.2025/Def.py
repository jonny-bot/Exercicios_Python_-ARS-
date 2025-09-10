def calcular_imposto(valor):

    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2

    return imposto

valor_produto1 = 1500
valor_produto2 = 3500

total_produto1 = calcular_imposto(valor_produto1)
total_produto2 = calcular_imposto(valor_produto2)

print(total_produto1)
print(total_produto2)