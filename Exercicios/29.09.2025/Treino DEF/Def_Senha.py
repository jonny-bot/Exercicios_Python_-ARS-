# Lidador de Senha

print('Confirmação de Senha')

def login_senha_correta():
    login_correto = 'joao'
    senha_correto = 'ars@3103'
    return login_correto, senha_correto

def login_senha_usuario():
    login_usuario = input('Login: ')
    senha_usuario = input('Senha: ')
    return login_usuario, senha_usuario

def validacao():
    if login_senha_usuario() == login_senha_correta():
        print('Acesso Liberado!!!')
    else:
        print('Acesso Negado!!!')

validacao()