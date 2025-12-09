'''

Desconto/Juros por pagamento
Leia preco, meio (pix, debito, credito) e parcelas.

Se meio em (pix, debito):
desconto de 10% se preco >= 100, senão 5%.
Se meio == 'credito':
se parcelas == 1, sem juros; se parcelas >= 2, acrescente 3% de juros.
Imprima o valor final.

'''

preco = float(input('Digite o Valor: '))

meio_pagamento = {
    1: 'pix',
    2: 'debito',
    3: 'credito'
}

print("Escolha a forma de pagamento:")
for chave, valor in meio_pagamento.items():
    print(f"{chave} - {valor}")

opcao = int(input("Digite o número da opção desejada: "))

forma = meio_pagamento.get(opcao, "Opção inválida")

if opcao == 1 and 2:
    if preco >= 100.0:
        preco = (preco * 0.90) # Desconto de 10%
        print(f'O Preço Final é de: R${preco:.2f}')

    else:
        preco = (preco * 0.95) # Desconto de 5%
        print(f'O Preço Final é de: R${preco:.2f}')

if opcao == 3:

    parcelas = int(input('Vamos Pagar em Quantas Parcelas: '))

    if parcelas == 1:
        print(f'Pagamento Sem Juros. O Valor Final é de: R${preco:.2f}')
    else:
        preco_final = preco * 1.03 # Juros de 3%
        print(f'Pagamento Com Juros. O Valor Final é de: R${preco_final:.2f}')

