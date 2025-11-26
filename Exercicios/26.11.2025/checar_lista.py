lista = ['Joao', 'Pedro', 'Fabio']

checar_nome = input('Digite um Nome: ')

nome_checado = False
for i in lista:
    if i == checar_nome:
        nome_checado = True

if nome_checado:
    print('O Nome Existe na Lista!')
else:
    print('O Nome Não Existe na Lista!')
