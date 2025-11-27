import json

with open('arquivo_JSON/exercicio1.json', 'r', encoding='utf-8') as f:
    usuarios = json.load(f)

for i in usuarios:
    nome = i.get('nome')
    idade = i.get('idade')
    homem = i.get('homem')
    peso = i.get('peso')
    altura = i.get('altura')

    print('Nome: ' + nome + ' || Idade: ' + str(idade) + ' || Homem: ' + str(homem) +
          ' || Peso: ' + str(peso) + ' || Altura: ' + str(altura))
