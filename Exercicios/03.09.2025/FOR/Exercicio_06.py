# Descobrir se o Número é primo.

numero = int(input('Digite um Número: '))

e_primo = True

if numero <= 1:
    e_primo = False

else:

    for var in range(2, numero):

        if numero % var == 0:
            e_primo = False
            break

if e_primo:
    print('O Número é PRIMO!!!')
else:
    print('O Número é não PRIMO!!!')