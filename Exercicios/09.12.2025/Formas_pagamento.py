valor = float(input('Digite o Valor: '))

formas_pagamento = {
    1: 'Dinheiro',
    2: 'Pix',
    3: 'Debito',
    4: 'Crédito'
}

pagamento = int(input('Digite a Forma de Pagamento: '))
conferencia = False
if pagamento in formas_pagamento:
    conferencia = True

if conferencia:
    print('Forma de Pagamento Existente!')
else:
    print('Forma de Pagamento Não Existente!')
