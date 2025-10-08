import random
import json

from numpy.ma.core import append

# Abre o arquivo JSON contendo as perguntas
with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

total_perguntas = int(input('Digite a quantidade de Perguntas: '))

perguntas = random.sample(perguntas, total_perguntas)

contagem_acertos = 0
contagem_erros = 0
lista_acertos = []
lista_erros = []

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    print(f'Categoria: {categoria}')
    print(f'{indice + 1}° Pergunta: {pergunta}')

    contagem = 1
    for alternativas in opcoes:
        print(f'{contagem}. {alternativas}')
        contagem += 1

    while True:
        try:
            resposta_correta = int(input("Digite um número inteiro entre 1 e 4: "))
            if resposta_correta in (1, 2, 3, 4):
                break
            else:
                print(f"Você digitou: {resposta_correta}, que não está entre 1 e 4. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if resposta_correta == correta:
        contagem_acertos += 1
        temp = ("Pergunta: " + pergunta + " - Categoria: " + categoria)
        lista_acertos.append(temp)

    else:
        contagem_erros += 1
        temp = ("Pergunta: " + pergunta + " - Categoria: " + categoria)
        lista_erros.append(temp)

cont_acertos = 1
print('======X Corretas X======')
for corretas in lista_acertos:
    print(f'{cont_acertos}° {corretas}')
    cont_acertos += 1

cont_erros = 1
print('======X Erradas X======')
for erradas in lista_erros:
    print(f'{cont_erros}° {erradas}\nA resposta correta é: {correta}')
    cont_erros += 1

print(f'{(contagem_acertos / total_perguntas) * 100:.2f}%\n'
      f'{(contagem_erros / total_perguntas) * 100:.2f}%')