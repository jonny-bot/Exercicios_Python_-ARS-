def login_senha():
    login = 'Joao'
    senha = 'ars@3103'
    return login, senha


def fazer_login_senha():
    fazer_login = input('Digite o Login: ')
    fazer_senha = input('Digite a Senha: ')
    return fazer_login, fazer_senha


adm_login, adm_senha = login_senha()
realiza_login, realiza_senha = fazer_login_senha()

autenticar = False
if realiza_login == adm_login and realiza_senha == realiza_senha:
    autenticar = True

if autenticar:
    print('Usuário Autenticado!')
else:
    print('Usuário ou Senha Incorretos!')
