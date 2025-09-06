nome = input('Informe seu nome completo: ').split()

print('Nome Maíusculo: ', ' '.join(nome).upper())

print('Nome minúsculo: ', ' '.join(nome).lower())

print('Quantas letras que o nome possue sem espaços: ', len(''.join(nome)))

print('Quantas letras tem o primeiro nome: ', len(nome[0]))