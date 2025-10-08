def valor_produto():
    produto_1 = 1500
    produto_2 = 2600
    return produto_1, produto_2

def calcular_imposto(valor):
    if valor > 2500:
        return valor * 0.30
    elif valor > 2000:
        return valor * 0.20
    elif valor > 1000:
        return valor * 0.10
    else:
        return valor * 0.40

produto_1, produto_2 = valor_produto()

imposto_1 = calcular_imposto(produto_1)
imposto_2 = calcular_imposto(produto_2)

print(f"Imposto do produto 1: R${imposto_1:.2f}")
print(f"Imposto do produto 2: R${imposto_2:.2f}")