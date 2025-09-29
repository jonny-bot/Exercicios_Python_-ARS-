# Criança (0-12) | Adolescente (13-17) | Adulto (18-64) | Idoso (64+)

def calc_idade():
    calc_idade = int(input('Qual a sua idade: '))
    return calc_idade

def verificacao_idade(verif_idade):
    if verif_idade <= 12:
        print('Criança')

    elif verif_idade <= 17:
        print('Adolescente')

    elif verif_idade <= 64:
        print('Adulto')

    else:
        print('Idoso')

classi = calc_idade()
verificacao_idade(classi)