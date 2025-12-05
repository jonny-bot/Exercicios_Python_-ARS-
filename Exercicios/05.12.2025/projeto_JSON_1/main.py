import json
import random

with open('Arquivos(Json)/exercicio1.json', 'r', encoding='utf-8') as xyz:
    usuarios = json.load(xyz)

    usuarios = random.sample(usuarios, 2)

    contador = 0
    for contador, i in enumerate(usuarios):
        nome = i.get('nome')
        idade = i.get('idade')
        homem = i.get('homem')
        peso = i.get('peso')
        altura = i.get('altura')

        contador += 1
        print(f'{contador}° Pessoal\n'
              f'Nome: {nome}\n'
              f'Idade: {idade}\n'
              f'Homem: {homem}\n'
              f'Peso: {peso}\n'
              f'Altura: {altura}\n')
