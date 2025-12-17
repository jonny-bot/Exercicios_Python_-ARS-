def login_senha_adm():
    login_adm = 'Joao'
    senha_adm = 'ars@3103'
    return login_adm, senha_adm


def fazer_login(login, senha):
    login_adm, senha_adm = login_senha_adm()
    if login == login_adm and senha == senha_adm:
        print('Acesso Liberado!')
    else:
        print('Acesso Negado!')


login = input('Login: ')
senha = input('Senha: ')
fazer_login(login, senha)
