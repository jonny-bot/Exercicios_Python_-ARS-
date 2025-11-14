import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

total_acertos = 0
total_erros = 0
lista_acertos = []
lista_erros = []

quantidade_pergunta = int(input('Digite a Quantidade de Perguntas: '))

perguntas = random.sample(perguntas, quantidade_pergunta)

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    print(f'Categoria: {categoria}\n'
          f'{indice + 1}° Pergunta: {pergunta}')

    contagem_alternativas = 0
    for alternativas in opcoes:
        contagem_alternativas += 1
        print(f'{contagem_alternativas}. {alternativas}')

    while True:
        try:
            resposta = int(input('Digite uma das Alternativas Corretas: '))

            if resposta in (1,2,3,4):

                if resposta == correta:
                    print('Parabêns. Você Acertou!!!')
                    total_acertos += 1
                    lista_acertos.append('Pergunta: ' + pergunta + ' | Categoria: ' + categoria)

                else:
                    print('Que Pena. Você Errou!!!\n'
                          f'A Resposta Correta é: {correta}')
                    total_erros += 1
                    lista_erros.append('Pergunta: ' + pergunta + ' | Categoria: ' + categoria + ' | Correta: ' + str(correta))

                break

            else:
                print(f'Você Digitou {resposta}. Que não está Entre 1 e 4.')

        except ValueError:
            print('Digite uma Entrada Válida!!!')

print(f'Total de Perguntas: {quantidade_pergunta}\n'
      f'Tota Acertos: {(total_acertos / quantidade_pergunta) * 100:.2f}\n'
      f'Tota Acertos: {(total_erros / quantidade_pergunta) * 100:.2f}\n')

if total_acertos > 0:
    contagem_acertos = 0
    print('Perguntas Corretas: ')
    for i in lista_acertos:
        contagem_acertos += 1
        print(f'{contagem_acertos}° {i}')

if total_erros > 0:
    contagem_erros = 0
    print('Perguntas Erradas: ')
    for j in lista_erros:
        contagem_erros += 1
        print(f'{contagem_erros}° {j}')
