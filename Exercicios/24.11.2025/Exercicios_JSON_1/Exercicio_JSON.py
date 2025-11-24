import json

with open('Arquivo_JSON/exercicio1.json', 'r', encoding='utf-8') as f:
    usuarios = json.load(f)

for i in usuarios:

    nome = i.get('nome')
    idade = i.get('idade')
    homem = i.get('homem')
    peso = i.get('peso')
    altura = i.get('altura')

    print(f'Nome: {nome} || Idade: {idade} || Homem: {homem} || Peso: {peso} || Altura: {altura}')
