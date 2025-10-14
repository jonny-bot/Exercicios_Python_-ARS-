import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

perguntas_acertadas = []
perguntas_erradas = []
soma_acertadas = 0
soma_erradas = 0

quantidade_pergunta = int(input('Qual a quantidade de perguntas: '))

perguntas = random.sample(perguntas, quantidade_pergunta)

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    print(f'Categoria: {categoria}\n'
          f'{indice + 1}° Pergunta: {pergunta}')

    print('=' * 40)

    contagem = 1
    for i in opcoes:
        print(f'{contagem}. {i}')
        contagem += 1

    print('=' * 40)

    while True:
        try:
            resposta = int(input('Digite um número inteiro entre 1 e 4: '))
            if resposta in (1, 2, 3, 4):
                break
            else:
                print(f'Você digitou: {resposta} que não está entre 1 e 4. Tente novamente.')
        except ValueError:
            print('Digite uma entrada válida.')

    if resposta == correta:
        print(f'Parabêns, Você acertou!!!\n'
              f'====================')
        soma_acertadas += 1
        temp = ("Pergunta: " + pergunta + " - Categoria: " + categoria)
        perguntas_erradas.append(temp)

    else:
        print(f'Que Pena, Você Errou!!!\n'
              f'A resposta Correta é: {correta}\n'
              f'====================')
        soma_erradas += 1
        temp = ("Pergunta: " + pergunta + " - Categoria: " + categoria)
        perguntas_acertadas.append(temp)

if soma_acertadas > 0:
    contagem_acertos = 1
    print('Perguntas Acertadas:')
    for i in perguntas_acertadas:
        print(f'{contagem_acertos}° {i}')
        contagem_acertos += 1

if soma_erradas > 0:
    contagem_erros = 1
    print('Perguntas Erradas:')
    for j in perguntas_erradas:
        print(f'{contagem_erros}° {j}')
        contagem_erros += 1

print('=' * 20)
print(f'Relatório de Desempenho:\n'
      f'Porcentagem de Acertos: {(soma_acertadas / quantidade_pergunta) * 100:.2f}%\n'
      f'Porcentagem de Erros: {(soma_erradas / quantidade_pergunta) * 100:.2f}%\n')
