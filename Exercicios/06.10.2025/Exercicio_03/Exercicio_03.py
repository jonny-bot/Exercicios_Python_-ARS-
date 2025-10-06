import random
import json

with open('JSON/exercicio3.json', 'r', encoding='utf-8') as f:
    usuarios = json.load(f)

usuarios = random.sample(usuarios, 1)

for indice, item in enumerate(usuarios):
    titulo = item.get("titulo")
    autor = item.get("autor")
    ano = item.get("ano")
    genero = item.get("genero")
    paginas = item.get("paginas")

    print(f'Nome do Livro: {titulo}\n'
          f'Autor da Obra: {autor}\n'
          f'Ano de Publicação: {ano}\n'
          f'Gênero: {genero}\n'
          f'Total de Páginas: {paginas}')