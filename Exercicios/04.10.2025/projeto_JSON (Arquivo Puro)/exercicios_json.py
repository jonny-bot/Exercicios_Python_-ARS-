import random  # Importa o módulo 'random' para gerar amostras aleatórias
import json    # Importa o módulo 'json' para manipular arquivos JSON

# Abre o arquivo JSON contendo as perguntas
with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)  # Carrega o conteúdo do arquivo como uma lista de dicionários

# Seleciona aleatoriamente 5 perguntas da lista
perguntas = random.sample(perguntas, 5)  # 'sample' retorna uma amostra de 5 itens sem repetição

# Itera sobre as perguntas selecionadas
for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")  # Obtém o valor da chave 'categoria' do dicionário
    pergunta = item.get("pergunta")    # Obtém o valor da chave 'pergunta' do dicionário

    # Exibe o índice e a categoria da pergunta
    print(f'{indice}: {categoria}')
    # Exibe o índice e o texto da pergunta
    print(f'{indice}: {pergunta}')
