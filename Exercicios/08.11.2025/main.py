def cadastro(nome, idade, sexo):

    print(f'Nome: {nome}\nIdade: {idade}\nSexo: {sexo}')

opcao = int(input('Digite 1: '))

if opcao == 1:

    nome = input('Digite o Seu Nome: ')

    idade = int(input('Digite a Idade: '))

    sexo = input('M - Masculino || F - Feminino\n'
                 'Digite seu Sexo: ').lower()

    if sexo == 'm':
        sexo = 'Masculino'
    else:
        if sexo == 'f':
            sexo = 'Feminino'

    cadastro(nome, idade, sexo)