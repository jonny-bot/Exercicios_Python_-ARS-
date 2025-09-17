'''

Categoria de atleta (encadeado)
Com base em idade, classifique: idade < 9 Mirim, 9–13 Infantil, 14–17 Juvenil, 18–39 Adulto, >=40 Master (use comparações do tipo 9 <= idade <= 13).

'''

idade = int(input('Digite a Idade do Atleta: '))

if idade <= 9:
    print('Mirim')
elif 9 <= idade <= 13:
    print('Infantil')
elif 14 <= idade <= 17:
    print('Juvenil')
elif 18 <= idade <= 39:
    print('Adulto')
else:
    print('Master')