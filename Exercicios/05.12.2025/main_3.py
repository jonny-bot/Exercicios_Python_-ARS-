lista = [1,2,3,4,5,6,7,8,9]


numero = int(input('Digite um Número: '))


verificacao = False
if numero in lista:
    verificacao = True


if verificacao:
    print('O Número Existe Na Lista!')
else:
    print('O Número Não Existe Na Lista!')
