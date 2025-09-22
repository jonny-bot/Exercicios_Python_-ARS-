login_correto = 'joao'
senha_correta = 'ars@2025'

while True:
    login_usuario = input('Digite o Login: ')
    senha_usuario = input('Digite a Senha: ')

    if login_usuario == login_correto and senha_usuario == senha_correta:
        print('Acesso Liberado!!!')
        break
    else:
        print('Acesso Negado!!!')