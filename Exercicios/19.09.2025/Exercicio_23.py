'''

Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento   Conceito
      Entre 9.0 e 10.0              A
      Entre 7.5 e 9.0               B
      Entre 6.0 e 7.5               C
      Entre 4.0 e 6.0               D
      Entre 4.0 e zero              E

    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
    se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

'''

def conceito(media):
    if media >= 0.0:
        print('Você tirou E')
        print('Você foi APROVADO')

    if media >= 4.0:
        print('Você tirou D')
        print('Você foi APROVADO')

    if media >= 6.0:
        print('Você tirou C')
        print('Você foi APROVADO')

    if media >= 7.5:
        print('Você tirou B')
        print('Você foi APROVADO')

    if media >= 9.0:
        print('Você tirou A')
        print('Você foi REPROVADO')

def verificador(med):

    verificar_media = False

    if media >= 0.0 and media <= 4.0:
        verificar_media = True
        conceito(media)

    if media >= 4.1 and media <= 6.0:
        verificar_media = True
        conceito(media)

    if media >= 6.1 and media <= 7.4:
        verificar_media = True
        conceito(media)

    if media >= 7.5 and media <= 8.9:
        verificar_media = True
        conceito(media)

    if media >= 9.0:
        verificar_media = True
        conceito(media)

nota_1 = float(input('Digite a 1° Nota: '))

nota_2 = float(input('Digite a 2° Nota: '))

media = (nota_1 + nota_2) / 2
print(f'Sua Média é: {media}')
verificador(media)