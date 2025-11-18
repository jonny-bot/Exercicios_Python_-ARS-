def analisar_idade(idade):
    if 5 <= idade <= 7:
        print('Infantil')

    elif 8 <= idade <= 10:
        print('Iniciado')

    elif 11 <= idade <= 13:
        print('Juvenil')

    elif 14 <= idade <= 17:
        print('Júnior')

    else:
        print('Sénior')



idade = int(input('Digite a Idade: '))

analisar_idade(idade)