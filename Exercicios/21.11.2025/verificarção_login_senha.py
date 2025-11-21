def login_senha_administrador():
    login = 'Joao'
    senha = 'ars@3103'

    return login, senha


def verificador_login_senha():
    login, senha = login_senha_administrador()

    login_usuario = input('Digite o Login: ')
    senha_usuario = input('Digite a Senha: ')

    if login_usuario == login and senha_usuario == senha:
        print('Acesso Liberado!!!')

    else:
        print('Acesso Negado!!!')

verificador_login_senha()
