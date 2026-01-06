import json

with open('Arquivos(Json)/exercicio1.json', 'r', encoding='utf-8') as xyz:
    usuarios = json.load(xyz)

    for i in usuarios:
        print(i['nome'],
              i['idade'],
              i['homem'],
              i['peso'],
              i['altura'],)
