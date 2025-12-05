import random
import json


with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

contador_acertos = 0
contador_erros = 0

lista_acertos = []
lista_erros = []

total_alternativas = int(input('Digite o Total de Perguntas: '))

perguntas = random.sample(perguntas, total_alternativas)

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get('opcoes')
    correta = item.get('correta')

    print(f'Categoria: {categoria}')
    print(f'{indice + 1}° Pergunta: {pergunta}')

    contador_alternativas = 0
    for alternativas in opcoes:
        contador_alternativas += 1
        print(f'{contador_alternativas}. {alternativas}')

    while True:
        try:

            escolha = int(input('Digite a Resposta Correta: '))

            if 1 <= escolha <= 4:

                if escolha == correta:
                    print('Parabéns. Você Acertou!!!')
                    contador_acertos += 1
                    temp = 'Pergunta: ' + pergunta + ' | Categoria: ' + categoria + ' | Correta: ' + str(correta)
                    lista_acertos.append(temp)

                else:
                    print('Que Pena. Você Errou!!!')
                    contador_erros += 1
                    temp = 'Pergunta: ' + pergunta + ' | Categoria: ' + categoria + ' | Correta: ' + str(correta)
                    lista_erros.append(temp)
                break

            else:
                print(f'Você Digitou {escolha}. Que não está entre 1 e 4.')

        except ValueError:
            print('Digite uma Entrada Válida!')

print('=====X Relatorio de Acertos e Erros X=====\n'
      f'Questões Total (is): {total_alternativas}\n'
      f'Acertos: {contador_acertos} - {((contador_acertos / total_alternativas) * 100):.2f} %\n'
      f'Erros: {contador_erros} - {((contador_erros / total_alternativas) * 100):.2f} %')

if contador_acertos > 0:
    print('Perguntas Corretas: ')
    contador_alternativas_acertos = 0
    for acertos in lista_acertos:
        contador_alternativas_acertos += 1
        print(f'{contador_alternativas_acertos}° {acertos}')

if contador_erros > 0:
    print('Perguntas Erradas: ')
    contador_alternativas_erros = 0
    for erros in lista_erros:
        contador_alternativas_erros += 1
        print(f'{contador_alternativas_erros}° {erros}')
