from datetime import date

'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''

atual = date.today().year

nasc = int(input("Ano de nascimento do(a) nadador(a): \n"))

idade = atual - nasc

print(f"O atleta tem {idade} anos em {atual}.")

if idade <= 9:
    print('Mirim')

elif idade <= 14:
    print('Infantil')

elif idade <= 19:
    print('Júnior')

elif idade == 20:
    print('Sênior')

else:
    print('Master')