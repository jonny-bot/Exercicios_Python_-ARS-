from random import choice

nome1 = input('1º aluno(a): ')

nome2 = input('2º aluno(a): ')

nome3 = input('3º aluno(a): ')

nome4 = input('4º aluno(a): ')

escolhido = choice([nome1, nome2, nome3, nome4])

print(f'O aluno escolhido foi: {escolhido}')