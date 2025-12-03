lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numero = int(input('Digite um Número: '))

autenticacao = False
if numero in lista:
    autenticacao = True

if autenticacao:
    print('O Número Existe na Lista!')
else:
    print('O Número Não Existe na Lista!')
