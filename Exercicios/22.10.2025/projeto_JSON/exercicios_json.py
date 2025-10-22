import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

#  quantidade_pergunta = int(input('Digite quantidade de Perguntas: '))

respostas_corretas = 0
respostas_erradas = 0
lista_respostas_corretas = []
lista_respostas_erradas = []

perguntas = random.sample(perguntas, 1)

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
                    print('Parabéns, Você Acertou!!!')
                    respostas_corretas += 1
                    corretas = ' pergunta: ' + pergunta + ' categoria: ' + categoria
                    lista_respostas_corretas.append(corretas)
                else:
                    print('Que pena, Você Errou!!!\n'
                          f'A Alternativa Correta é: {correta}')
                    respostas_erradas += 1
                    erradas = ' pergunta: ' + pergunta + ' categoria: ' + categoria
                    lista_respostas_erradas.append(erradas)
                break
        except ValueError:
            print("Erro: por favor, digite um número inteiro válido.")

print(f'Perguntas Corretas: {lista_respostas_corretas}')
print(f'Perguntas Erradas: {lista_respostas_erradas}')
