'''

Desconto/Juros por pagamento
Leia preco, meio (pix, debito, credito) e parcelas.

Se meio em (pix, debito): desconto de 10% se preco >= 100, senão 5%.
Se meio == 'credito': se parcelas == 1, sem juros; se parcelas >= 2, acrescente 3% de juros. Imprima o valor final.

'''

preco = float(input('Digite o Preço: '))

print('P - Pix || D - Débito || C - Crédito')
forma_pagamento = input('Digite a forma de pagamento: ')

if forma_pagamento == 'p'.lower() and preco >= 100:
    total = (10 / 100) * preco
    print(f'O valor do Produto é: R${preco}')
    print(f'O valor com Desconto: R${total}')
    print(f'Valor com Desconto: R${preco - total}')

if forma_pagamento == 'd'.lower():
    total = (5 / 100) * preco
    print(f'O valor do Produto é: R${preco}')
    print(f'O valor com Desconto: R${total}')
    print(f'Valor com Desconto: R${preco - total}')

if forma_pagamento == 'c'.lower():

    parcelas = int(input('Gostaria de Parcelar em quantas Vezes: '))
    print('=======================================')
    if parcelas == 1:
        total = preco
        print(f'O valor total fica: R${total}')

    else:
        total = preco + (preco * 0.03)
        print(f'O valor fica: R${total}')