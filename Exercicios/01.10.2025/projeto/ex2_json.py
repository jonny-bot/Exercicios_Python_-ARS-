import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as xyz:
    perguntas = json.load(xyz)


jogadas = int(input('Você quer jogar quantas vezes: '))


perguntas = random.sample(perguntas, jogadas)  # sample pega uma amostra, nesse caso do perguntas pegando 5 itens


placar = 0


for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    # assim por diante
    print(f'{indice}: {categoria}')
    print(f'{indice}: {pergunta}')
    print('Alternativas: ')


    contador = 0
    for i in opcoes:
        contador += 1
        print(f'{contador}. {i}')


    resposta = int(input('Qual a alternativa correta: '))


    if resposta == correta:
        print('Parabêns, você acertou!!!')
        placar += 1

    else:
        print('Que Pena, Você Errou!!!')


print(f'De {jogadas} jogadas, você: Acertou {placar} e Errou {jogadas-placar}')