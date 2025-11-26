import json

with open('arquivo_JSON/exercicio1.json', 'r', encoding='utf-8') as f:
    usuarios = json.load(f)

'''
for i in usuarios:
    nome = i.get('nome')
    idade = i.get('idade')
    homem = i.get('homem')
    peso = i.get('peso')
    altura = i.get('altura')
'''

checar_nome = input('Digite um Nome: ')

nome_checado = False
for i in usuarios:
    if i.get('nome') == checar_nome:
        nome_checado = True

if nome_checado:
    print('O Nome Consta na Lista!')
else:
    print('O Nome Não Consta na Lista!')
