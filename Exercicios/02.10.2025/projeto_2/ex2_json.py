import random
import json

with open('Exercicios_JSON/exercicio2.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

rodadas = int(input("Vamos ter quantas rodadas: "))
print('============ x ============')

perguntas = random.sample(perguntas, rodadas) # sample pega uma amostra, nesse caso do perguntas pegando 5 itens

acertos_total = 0
erros_total = 0
perguntas_acertadas = []
perguntas_erradas = []

for indice, item in enumerate(perguntas):
    categoria = item.get("categoria")
    pergunta = item.get("pergunta")
    opcoes = item.get('opcoes')
    correta = item.get('correta')
    # assim por diante
    # print(f'{indice + 1} - {categoria}')
    print(f'{indice + 1}° Pergunta de {rodadas}: {pergunta} ({categoria})')

    contador = 0
    for i in opcoes:
        contador += 1
        print(f'{contador}. {i}')

    print('============ x ============')
    resposta_correta = str(input('Qual a sua resposta correta: '))

    while True:
        try:
            resposta_correta = int(input("Digite um número inteiro entre 1 e 4: "))
            if resposta_correta in (1, 2, 3, 4):
                print(f"Você digitou um número válido: {resposta_correta}")
                break  # Sai do loop se a entrada for válida
            else:
                print(f"Você digitou: {resposta_correta}, que não está entre 1 e 4. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if int(resposta_correta) == correta:
        print('A resposta está correta!!!')
        acertos_total += 1
        temp = ("Pergunta: " + pergunta +
                " - Categoria: " + categoria)
        perguntas_acertadas.append(temp)
        print('============ x ============')

    else:
        print('Que pena, você ERROU!!!')
        erros_total += 1
        print(f'A Resposta correta é: {correta}')
        temp = ("Pergunta: " + pergunta +
                " - Categoria: " + categoria)
        perguntas_erradas.append(temp)
        print('============ x ============')

    print(f'De {rodadas} Rodadas:\n'
          f'Você Acertou {acertos_total} X Errou {erros_total}\n'
          f'Porcentagem de Acertos: {(acertos_total / rodadas) * 100}\n'
          f'Porcentagem de Erros: {(erros_total / rodadas) * 100}\n'
          f'============ x ============')

print('Relátorio de Desempenho:')

perg_certa = 0
print(f'✅ Perguntas Certas: ')
for j in perguntas_acertadas:
    perg_certa += 1
    print(f'{perg_certa}° {j} ')

perg_errada = 0
print('============ x ============')
print(f'❌ Perguntas Erradas: ')
for h in perguntas_erradas:
    perg_errada += 1
    print( f'{perg_errada}° {h} \n'
          f'A Resposta Correta é: {correta}')