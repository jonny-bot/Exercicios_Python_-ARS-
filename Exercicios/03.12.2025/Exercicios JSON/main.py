import random
import json

with open('exercicio.json','r', encoding='utf-8') as xyz:
    perguntas = json.load(xyz)

contador_sim = 0

perguntas = random.sample(perguntas, 8)

for indice,i in enumerate(perguntas):
    pergunta = i.get('pergunta')

    print(f'{indice + 1}° Pergunta: {pergunta}')

    while True:
        try:

            opcao = int(input('1 - Sim || 2 Não\n'
                              'Digite umas das Opções: '))

            if 1 <= opcao <= 2:

                if opcao == 1:
                    contador_sim += 1
                    break

                elif opcao == 2:
                    contador_sim -= 1
                    break

            else:
                print(f'Você Digitou {opcao}. Que não está entre 1 e 2.')

        except ValueError:
            print('Digite uma Entrada Válida!')


if contador_sim < 1:
    print("Inocente!!!")

elif contador_sim <= 3:
    print("Suspeita!!!")

elif contador_sim <= 7:
    print("Cúmplice!!!")

elif contador_sim == 8:
    print("Assassino!!!")
