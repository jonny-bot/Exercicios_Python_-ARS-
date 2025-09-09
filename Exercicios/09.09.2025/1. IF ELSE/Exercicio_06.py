Idade = int(input('Digite um Número: '))

if Idade <= 12:
    print(f'Criança de {Idade} anos!!!')
elif Idade <= 17:
    print(f'Adolescente de {Idade} anos!!!')
elif Idade <= 64:
    print(f'Adulto de {Idade} anos!!!')
else:
    print(f'Idoso de {Idade}!!!')