import json

with open('arquivo_JSON/exercicio1.json', 'r', encoding='utf-8') as f:
    usuarios = json.load(f)

checar_login = input('Digite o Login: ')
checar_senha = input('Digite a Senha: ')

autenticado = False
for i in usuarios:
    if i.get('login') == checar_login and i.get('senha') == checar_senha:
        autenticado = True

if autenticado:
    print('Usuário Autenticado!')

    for i in usuarios:
        print(f'Login: {i['login']} || Senha: {i['senha']} || Situação: {i['situacao']} || Saldo: {i['saldo']}')

else:
    print('Login ou Senha incorreto!')

