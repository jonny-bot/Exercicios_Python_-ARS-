lista = ['joao', 'pedro', 'natalia']

nome = input('Digite um Nome: ')

verificacao = False
if nome in lista:
    verificacao = True

if verificacao:
    print('O Nome Consta na Lista!')
else:
    print('O Nome Não Consta na Lista!')
