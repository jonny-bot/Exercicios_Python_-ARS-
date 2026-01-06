import random
import json


def abrir_arquivos():
    with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
        perguntas = json.load(f)

    return perguntas


def gerar_perguntas(perguntas_total):
    perguntas = random.sample(abrir_arquivos(), perguntas_total)
    return perguntas


perguntas_total = int(input('Quantas Perguntas vão ser Geradas: '))


lista_acertos = []
lista_erros = []
contagem_acertos = 0
contagem_erros = 0


def perguntas():
    global contagem_acertos, contagem_erros, lista_acertos, lista_erros

    for indice, item in enumerate(gerar_perguntas(perguntas_total)):
        categoria = item.get("categoria")
        pergunta = item.get("pergunta")
        opcoes = item.get("opcoes")
        correta = item.get("correta")

        print(f'Categoria: {categoria}\n'
              f'{indice + 1}° Pergunta: {pergunta}')

        contador = 0
        for alternativas in opcoes:
            print(f'{contador + 1}. {alternativas}')
            contador += 1

        while True:

            try:

                resposta = int(input("Digite a Alternativa Correta: "))

                if 1 <= resposta <= len(opcoes):

                    if resposta == correta:
                        print("Parabéns! Você Acertou!")
                        contagem_acertos += 1
                        lista_acertos.append(f'Pergunta: {pergunta} | Categoria: {categoria}')

                    else:
                        print("Que Pena, Você Errou!")
                        contagem_erros += 1
                        lista_erros.append(f'Pergunta: {pergunta} | Categoria: {categoria} | Correta: {correta}')

                    break

                else:
                    print(f"Você digitou {resposta}, que não está entre 1 e {len(opcoes)}.")

            except ValueError:
                print("Digite uma Entrada Válida Apenas Números.")

perguntas()

if contagem_acertos > 0:
    print('Lista de Acertos: ')
    contador_acertos = 0
    for i in lista_acertos:
        print(f'{contador_acertos + 1}° {i}')
        contagem_acertos += 1

if contagem_erros > 0:
    contador_erros = 0
    print('Lista de Erros: ')
    for j in lista_erros:
        print(f'{contador_erros + 1}° {j}')
        contador_erros += 1
