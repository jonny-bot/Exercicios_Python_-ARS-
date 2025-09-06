numero = input('Informe o número: ')

numero = int(numero)

uni = numero // 1 % 10

de = numero // 10 % 10

ce = numero // 100 % 10

mi = numero // 1000 % 10

print(f'Unidade: {uni} \nDezena: {de} \nCentena: {ce} \nMilhar: {mi}'.format())