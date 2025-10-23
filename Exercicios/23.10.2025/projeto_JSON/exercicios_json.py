import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

respostas_corretas = 0
respostas_erradas = 0
lista_respostas_corretas = []
lista_respostas_erradas = []

quantidade_pergunta = int(input('Digite quantidade de Perguntas: '))

perguntas = random.sample(perguntas, quantidade_pergunta)

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    print(f'Categoria: {categoria}\n'
          f'{indice + 1}° Pergunta: {pergunta}')

    contagem = 0
    for alternativas in opcoes:
        contagem += 1
        print(f'{contagem}. {alternativas}')

    while True:
        try:
            alternativa_escolhida = int(input('Digite a alternativa correta (1 a 4): '))
            if alternativa_escolhida not in (1, 2, 3, 4):
                print("Digite uma entrada válida entre 1 e 4.")
            else:
                if alternativa_escolhida == correta:
                    print('Parabéns, Você Acertou!!!\n'
                          '======= X =======')
                    respostas_corretas += 1
                    corretas = ' Pergunta: ' + pergunta + ' Categoria: ' + categoria
                    lista_respostas_corretas.append(corretas)
                else:
                    print('Que pena, Você Errou!!!\n'
                          f'A Alternativa Correta é: {correta}\n'
                          f'======= X =======')
                    respostas_erradas += 1
                    erradas = ' Pergunta: ' + pergunta + ' Categoria: ' + categoria
                    lista_respostas_erradas.append(erradas)
                break
        except ValueError:
            print("Erro: por favor, digite um número inteiro válido.")

print(f'======= X =======\n'
      f'Relatório:\n'
      f'Perguntas Corretas: {(respostas_corretas / quantidade_pergunta) * 100:.2f}%\n'
      f'Perguntas Erradas: {(respostas_erradas / quantidade_pergunta) * 100:.2f}%\n'
      f'======= X =======')

if respostas_corretas > 0:
    print('Perguntas Corretas:')
    contagem_correta = 0
    for perguntas_corretas in lista_respostas_corretas:
        contagem_correta += 1
        print(f'{contagem_correta}°{perguntas_corretas}')

if respostas_erradas > 0:
    print('Perguntas Erradas:')
    contagem_erradas = 0
    for perguntas_erradas in lista_respostas_erradas:
        contagem_erradas += 1
        print(f'{contagem_erradas}°{perguntas_erradas}')