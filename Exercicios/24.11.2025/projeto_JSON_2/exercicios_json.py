import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

contagem_acertos = 0
contagem_erros = 0
lista_perguntas_acerto = []
lista_perguntas_erros = []

total_perguntas = int(input('Digite o Total de Produtos: '))

perguntas = random.sample(perguntas, total_perguntas)

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    print(f'Categoria: {categoria}')
    print(f'{indice + 1}° Pergunta: {pergunta}')

    contagem_alternativas = 0
    for alternativas in opcoes:
        contagem_alternativas += 1
        print(f'{contagem_alternativas}. {alternativas}')

    while True:
        try:

            alternativa_escolhida = int(input(f'Pergunta: {indice + 1} de {total_perguntas}\n'
                                              'Digite a Alternativa Correta: '))

            if 1 <= alternativa_escolhida <= 4:

                if alternativa_escolhida == correta:
                    print('Parabêns. Você Acertou!!!')
                    contagem_acertos += 1
                    temp = 'Pergunta: ' + pergunta + ' Categoria: ' + categoria
                    lista_perguntas_acerto.append(temp)
                    break

                else:
                    print('Que Pena. Você Errou!!!')
                    contagem_erros += 1
                    temp = 'Pergunta: ' + pergunta + ' Categoria: ' + categoria + ' Correta: ' + str(correta)
                    lista_perguntas_erros.append(temp)
                    break

            else:
                print(f'Você Digitou {alternativa_escolhida}. Que não está entre 1 e 4.')

        except ValueError:
            print('Digite Uma Entrada Válida!!!')

if contagem_acertos > 0:
    print('Perguntas Corretas: ')
    for perguntas_corretas in lista_perguntas_acerto:
        print(perguntas_corretas)

if contagem_erros > 0:
    print('Perguntas Erradas: ')
    for perguntas_erradas in lista_perguntas_erros:
        print(perguntas_erradas)

print('Placar de Acertos X Erros: \n'
      f'Acertos: {((contagem_acertos / total_perguntas) * 100):.2f}%\n'
      f'Erros: {((contagem_erros / total_perguntas) * 100):.2f}%')
