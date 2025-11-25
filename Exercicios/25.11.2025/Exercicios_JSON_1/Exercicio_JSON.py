import json

with open('Arquivo_JSON/exercicio1.json', 'r', encoding='utf-8') as f:
    usuarios = json.load(f)

nome_procurado = input('Qual Nome Você está Procurando: ')

encontrado = False
for i in usuarios:
    if i.get('nome') == nome_procurado:
        encontrado = True
        break

if encontrado:
    print('O Nome Existe na Lista!')
else:
    print('O Nome Não Existe na Lista!')
