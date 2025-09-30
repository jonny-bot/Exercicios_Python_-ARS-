def par_impar():
    numero = int(input('Digite um Número: '))
    return numero


def verificacao(num):
    if num % 2 == 0:
        print('É PAR!!!')
    else:
        print('É IMPAR!!!')
        

num = par_impar()
verificacao(num)