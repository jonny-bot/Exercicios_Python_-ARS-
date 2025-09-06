idade = int(input('Digite a Idade da Pessoa: \n'))

if idade <= 12:
    print(f'Essa pessoa é uma CRIANÇA de {idade} anos!!!')
elif idade <= 17:
    print(f'Essa pessoa é um ADOLESCENTE de {idade} anos!!!')
elif idade <= 64:
    print(f'Essa pessoa é um ADULTO de {idade} anos!!!')
else:
    print(f'Essa pessoa é um IDOSO de {idade} anos!!!')