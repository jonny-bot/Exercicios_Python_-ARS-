senha_correta = 'ars@2025'

while True:
    senha = input('Digite a senha: ')
    if senha == senha_correta:
        print('Senha Correta')
        break
    else:
        print('Senha Incorreta!!!')