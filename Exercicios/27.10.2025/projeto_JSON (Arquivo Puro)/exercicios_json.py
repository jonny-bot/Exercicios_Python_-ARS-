import random
import json

from pyparsing import White

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

lista_corretas = []
lista_erradas = []
perguntas_corretas = 0
perguntas_erradas = 0

quantidade_pergunta = int(input('Quantas Perguntas: '))

perguntas = random.sample(perguntas, quantidade_pergunta)

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    print(f'Categoria: {categoria}')
    print(f'{indice + 1}° Pergunta: {pergunta}')

    contagem = 0
    for alternativas in opcoes:
        contagem += 1
        print(f'{contagem} - {alternativas}')

    while True:
        try:
            alternativa_escolhida = int(input('Digite a alternativa correta: '))
            if alternativa_escolhida not in (1,2,3,4):
                print('Digite um Número Inteiro Válido')
            else:
                if alternativa_escolhida == correta:
                    print('Parabêns, Você Acertou!!!')
                    perguntas_corretas += 1
                    temp = 'Pergunta: ' + pergunta + ' Categoria: ' + categoria
                    lista_corretas.append(temp)
                else:
                    print('Que Pena, Você Errou!!!\n'
                          f'a Resposta Correta é: {correta}')
                    perguntas_erradas += 1
                    temp = 'Pergunta: ' + pergunta + ' Categoria: ' + categoria
                    lista_erradas.append(temp)
                break
        except ValueError:
            print('Digite uma entrada válida!!!')

print('Relátorio de Desempenho:\n'
      f'Acertos: {(perguntas_corretas / quantidade_pergunta) * 100:.2f}%\n'
      f'Erradas: {(perguntas_erradas / quantidade_pergunta) * 100:.2f}%')

if perguntas_corretas > 0:
    print('Perguntas Corretas:')
    for indice, pergunta in enumerate(lista_corretas, 1):
        print(f"{indice}° {pergunta}")

if perguntas_erradas > 0:
    print('Perguntas Erradas:')
    for indice, pergunta in enumerate(lista_erradas, 1):
        print(f"{indice}° {pergunta}")
