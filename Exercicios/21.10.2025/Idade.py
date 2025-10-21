'''

Infantil 5 - 7 anos
Iniciado 8 - 10 anos
Juvenil 11 - 13 anos
Junior 14 - 17 anos
Sénior Maiores de 18 anos

'''

def idade(idade):
    if idade <= 7:
        print('Infantil')
    elif idade <= 10:
        print('Iniciado')
    elif idade <= 13:
        print('Juvenil')
    elif idade <= 17:
        print('Junior')
    else:
        print('Sénior')
    return idade

mostrar_idade = idade(7)
print(mostrar_idade)