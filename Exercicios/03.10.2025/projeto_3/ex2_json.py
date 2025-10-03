import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

quantas_perguntas = int(input('Quantas Perguntas: '))

acertos_total = 0
erros_total = 0
lista_acertos = []
lista_erros = []

perguntas = random.sample(perguntas, quantas_perguntas) # sample pega uma amostra, nesse caso do perguntas pegando 5 itens
for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get('correta')
    # assim por diante
    print(f'Categoria: {categoria}')
    print(f'{indice + 1}° Pergunta: {pergunta}')

    contador = 1
    for alternativas in opcoes:
        print(f'{contador}. {alternativas}')
        contador += 1

    resposta = str(input('Qual a Resposta Correta: '))

    lista = ['1','2','3','4']

    while resposta not in (lista):

        print('Digite apenas Números de 1 a 4')
        resposta = str(input('Qual a Resposta Correta: '))

    if int(resposta) == correta:
        print('Parabens Você Acertou!!!\n'
              '=====X  X=====')
        acertos_total += 1
        temp = ("Pergunta: " + pergunta +
                " - Categoria: " + categoria)
        lista_acertos.append(temp)
    else:
        print('Que pena, você Errou!!!\n'
              '=====X  X=====')
        erros_total += 1
        print(f'A Resposta correta é: {correta}\n'
              f'=====X  X=====')
        temp = ("Pergunta: " + pergunta +
                " - Categoria: " + categoria)
        lista_erros.append(temp)

print(f'=====X Placar: X=====\n'
      f'De {quantas_perguntas} Rodadas:\n'
      f'Acertou ✅ {acertos_total} ✅ X ❌ {erros_total} ❌ Errou\n'
      f'Acertos: {(acertos_total / quantas_perguntas) * 100} %\n'
      f'Erros: {(erros_total / quantas_perguntas) * 100} %')

print('=====X Relátorio de Desempenho X=====')

contador_acertos = 1
print("✅ Perguntas Corretas ✅ : ")
for i in lista_acertos:
    print(f'{contador_acertos}° {i}\n')
    contador_acertos += 1

contador_erros = 1
print("❌ Perguntas Erradas ❌ : ")
for j in lista_erros:
    print(f'{contador_erros}° {j} \n'
          f'A Resposta Correta é: {correta}')
    contador_erros += 1