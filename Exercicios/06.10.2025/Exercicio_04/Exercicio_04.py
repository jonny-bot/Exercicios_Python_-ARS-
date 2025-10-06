import random
import json

from scipy.constants import value

with open('JSON/exercicio4.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

perguntas = random.sample(perguntas, 1) # sample pega uma amostra, nesse caso do perguntas pegando 5 itens
for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    print(f'Categoria: {categoria}\n'
          f'{indice + 1}° Pergunta: {pergunta}')

    contador = 1
    for alternativas in opcoes:
        print(f'{contador} - {alternativas}')
        contador += 1

    while True:
        try:
            print('======X Alternativa X======')
            alternativa = str(input("Digite um número inteiro entre 1 e 4: "))
            if alternativa in ('1', '2', '3', '4'):
                break
            else:
                print(f"Você digitou: {alternativa}, que não está entre 1 e 4. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if int(alternativa) == correta:
        print('Parabêns, você Acertou!!!')

    else:
        print('Que pena, você Errou!!!\n'
              f'A Alternativa correta é a: {correta}')