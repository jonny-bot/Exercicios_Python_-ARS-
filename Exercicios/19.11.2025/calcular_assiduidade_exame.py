def calcular_assiduidade(total_dias_trabalhados, dias_trabalhados):

    falta = total_dias_trabalhados - dias_trabalhados

    assiduidade = ((total_dias_trabalhados - falta) / total_dias_trabalhados) * 100

    print(f'Assiduidade: {assiduidade:.2f}%')

    return assiduidade


def calcular_nota(nota_exame):

    print(f'A Nota do Exame é de: {(nota_exame / 100) * 100}')

    return nota_exame


def situacao():
    total_dias_trabalhados = int(input('Digite o Total de Dias Trabalhados: '))

    dias_trabalhados = int(input('Total de Dias Trabalhados: '))

    nota_exame = int(input('Digite a nota do Exame:'))

    assiduidade = calcular_assiduidade(total_dias_trabalhados, dias_trabalhados)

    exame = calcular_nota(nota_exame)

    if assiduidade < 100 * 0.75:
        print('Reprovado!!!')

    elif assiduidade >= 100 * 0.75 and exame <= 5.0:
        print('Reprovado!!!')

    elif assiduidade >= 100 * 0.75 and 5 <= exame <= 9.5:
        print('Exame!!!')

    elif assiduidade >= 100 * 0.75 and 10 <= exame <= 20:
        print('Aprovado!!!')

situacao()
