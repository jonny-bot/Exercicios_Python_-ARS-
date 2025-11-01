def par_impar(numero):
    return numero % 2 == 0

verificar_numero = int(input('Digite um Número: '))

if par_impar(verificar_numero):
    print('O Número é PAR!!!')
else:
    print('O Número é IMPAR!!!')