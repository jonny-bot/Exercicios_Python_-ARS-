def media(nota1, nota2):
    return (nota1 + nota2) / 2

def int_media():
    nota1 = int(input('Digite a 1° Nota: '))
    nota2 = int(input('Digite a 2° Nota: '))
    resultado = media(nota1,nota2)
    print(f'A sua 1°Nota é {nota1}, e a 2°Nota é {nota2}. E a sua Média é {resultado}')
    return resultado

def classificacao_imc(class_imc):
    if class_imc < 5:
        print('O Aluno está Reprovado!!!')

    elif class_imc < 7:
        print('O Aluno está de Recuperação!!!')

    else:
        print('O Aluno está Aprovado!!!')

resul_imc = int_media()
classificacao_imc(resul_imc)