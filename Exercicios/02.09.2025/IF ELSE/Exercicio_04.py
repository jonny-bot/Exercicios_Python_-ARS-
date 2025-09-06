Nota_1 = int(input('Digite a 1° Nota: \n'))

Nota_2 = int(input('Digite a 2° Nota: \n'))

media = (Nota_1 + Nota_2) / 2

if media < 5:
    print('O aluno está REPROVADOR!!!')
elif media <= 7:
    print('O aluno está de RECUPERAÇÃO!!!')
else:
    print('O aluno está APROVADO!!!')