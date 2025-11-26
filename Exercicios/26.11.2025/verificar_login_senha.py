def login_senha():
    login_adm = 'Joao'
    senha_adm = 'ars@3103'

    return login_adm, senha_adm

login_adm, senha_adm = login_senha()

login = input('Digite o Login: ')
senha = input('Digite a Senha: ')

if login == login_adm and senha == senha_adm:
    print('Usuário Autenticados!')
else:
    print('Usuário ou Senha Incorretos!')
