def notas_provas():
    nota_p1 = int(input('Digita a 1° Nota da P1: '))
    nota_p2 = int(input('Digita a 2° Nota da P2: '))

    media_prova = (nota_p1 + nota_p2) / 2

    return media_prova


def notas_atividades():
    nota_atividades1 = int(input('Digita a 1° Nota da Atividade 1: '))
    nota_atividades2 = int(input('Digita a 2° Nota da Atividade 2: '))

    media_atividade = (nota_atividades1 + nota_atividades2) / 2

    return media_atividade


def calcular_medias():

    media_geral = (notas_provas() + notas_atividades()) / 2

    return media_geral


def situacao():

    media_calculada = calcular_medias()

    if media_calculada <= 5.0:
        print(f'Sua Média é {media_calculada} Você está de Reprovado!')

    elif media_calculada <= 7.0:
        print(f'Sua Média é {media_calculada} Você está de Exame!')

    else:
        print(f'Sua Média é {media_calculada} Você está Aprovado!')

situacao()