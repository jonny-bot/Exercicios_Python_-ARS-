import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as xyz:
    perguntas = json.load(xyz)


jogadas = int(input('Você quer jogar quantas vezes: '))


perguntas = random.sample(perguntas, jogadas)  # sample pega uma amostra, nesse caso do perguntas pegando 5 itens


placar_acertos = 0
placar_erros = 0


for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    # assim por diante
    # print(f'{indice + 1} - {categoria}')
    print('===========================')
    print(f'{indice + 1} - {pergunta}')
    print('===========================')
    print('Alternativas: ')


    contador = 0
    for i in opcoes:
        contador += 1
        print(f'{contador}. {i}')


    print('===========================')
    resposta = int(input('Qual a alternativa correta: '))
    print('===========================')


    while resposta not in (1,2,3,4):
        print('Digite apenas Números Válidos: ')
        resposta = int(input('Qual a alternativa correta: '))


    if resposta == correta:
        print('Parabêns, você acertou!!!')
        print('===========================')
        placar_acertos += 1

    else:
        print('Que Pena, Você Errou!!!')
        placar_erros += 1
        print(f'A Resposta Correta é a: {correta}')
        print('===========================')

print(f'==== x PLACAR x ====\n'
      f'De {jogadas} jogadas, você: Acertou {placar_acertos} X Erros {placar_erros}\n'
      f'Porcentagem de Acertos: {(placar_acertos / jogadas) * 100:.2f}%.\n'
      f'Porcentagem de Erros: {((placar_erros) / jogadas) * 100:.2f}%')