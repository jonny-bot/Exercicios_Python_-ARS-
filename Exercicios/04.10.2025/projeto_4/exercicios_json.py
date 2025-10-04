import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

quatidade_perguntas = int(input('Digite a Quantidade de Perguntas: '))

acertos_total = 0
erros_total = 0
lista_acertos = []
lista_erros = []

perguntas = random.sample(perguntas, quatidade_perguntas)

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get("opcoes")
    correta = item.get("correta")

    print(f'======X Perguntas X======\n'
          f'Categoria: {categoria}\n'
          f'{indice + 1}° Pergunta: {pergunta}')

    contador_alternativas = 1
    for alternativas in opcoes:
        print(f'({contador_alternativas}). {alternativas}')
        contador_alternativas += 1

    while True:
        try:
            print('======X Alternativa X======')
            alternativa = str(input("Digite um número inteiro entre 1 e 4: "))
            if alternativa in ('1', '2', '3', '4'):
                break  # Sai do loop se a entrada for válida
            else:
                print(f"Você digitou: {alternativa}, que não está entre 1 e 4. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if int(alternativa) == correta:
        print('Parabêns, Você Acertou a Questão!!!\n')
        acertos_total += 1
        temp = ("Pergunta: " + pergunta +
                " - Categoria: " + categoria)
        lista_acertos.append(temp)

    else:
        print(f'Que pena, Você Errou a Questão!!!\n'
              f'A Resposta Correta é: {correta}\n')
        erros_total += 1
        temp = ("Pergunta: " + pergunta +
                " - Categoria: " + categoria)
        lista_erros.append(temp)

print(f'======X Relátorio de Desempenho X======\n'
      f'Quantidade de Acertos: {acertos_total} - '
      f'Porcentagem: {(acertos_total / quatidade_perguntas) * 100:.2f}%\n'
      f'Quantidade de Erros: {erros_total} - '
      f'Porcentagem: {(erros_total / quatidade_perguntas) * 100:.2f}%\n'
      f'======X Relátorio de Desempenho X======')

contador_acertos = 0
print('===x Lista de Acertos x===')
for i in lista_acertos:
    contador_acertos += 1
    print(f'{contador_acertos}° {i}')

contador_erros = 0
print(f'===x Lista de Erros x===')
for j in lista_erros:
    contador_erros += 1
    print(f'{contador_erros}° {j}\n'
          f'Resposta Correta: {correta}')