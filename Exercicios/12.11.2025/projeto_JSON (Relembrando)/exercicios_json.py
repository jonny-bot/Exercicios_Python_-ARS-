import random
import json

perguntas_corretas = []
perguntas_erradas = []
contagem_corretas = 0
contagem_erradas = 0

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

total_perguntas = int(input('Digite o Total de Perguntas: '))

perguntas = random.sample(perguntas, total_perguntas)

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    print(f'Categoria: {categoria}\n'
          f'{indice + 1}° Pergunta: {pergunta}')

    alternativas = 0
    for i in opcoes:
        alternativas += 1
        print(f'{alternativas}. {i}')

    contagem = 0

    while contagem < total_perguntas:
        try:
            resposta = int(input('Digite a Alternativa Correta: '))

            if resposta < 1 or resposta > 4:
                print(f'Você Digitou {resposta}. Que não está entre 1 e 4.')

            if resposta == correta:
                print('Parabêns. Você Acertou!!!')
                contagem += 1
                contagem_corretas += 1

                temp = 'Pergunta: ' + pergunta + ' Categoria: ' + categoria
                perguntas_corretas.append(temp)
                break

            else:
                print('Que pena. Você Errou!!!\n'
                      f'A alternativa Correta é: {correta}')
                contagem += 1
                contagem_erradas += 1

                temp = 'Pergunta: ' + pergunta + ' Categoria: ' + categoria + ' Correta: ' + str(correta)
                perguntas_erradas.append(temp)
                break

        except ValueError:
            print('Digite Uma Entrada Válida!!!')

if contagem_corretas > 0:
    total_corretas = 0
    print('Perguntas Corretas: ')
    for j in perguntas_corretas:
        total_corretas += 1
        print(f'{total_corretas}° {j}')

if contagem_erradas > 0:
    total_erradas = 0
    print('Perguntas Erradas: ')
    for h in perguntas_erradas:
        total_erradas += 1
        print(f'{total_erradas}° {h}')

print(f'Porcentagem de Acertos: {((contagem_corretas / total_perguntas) * 100):.2f}%\n'
      f'Porcentagem de Erradas: {((contagem_erradas / total_perguntas) * 100):.2f}%')