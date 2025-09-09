Nota_1 = int(input('Digite a 1° Nota: '))

Nota_2 = int(input('Digite a 2° Nota: '))

Media = (Nota_1 + Nota_2) / 2

if Media >= 7:
    print(f'O Aluno tirou {Media} e está Aprovado!!!')
elif Media >= 5:
    print(f'O Aluno tirou {Media} e está Recuperação!!!')
else:
    print(f'O Aluno tirou {Media} e está Reprovado!!!')

