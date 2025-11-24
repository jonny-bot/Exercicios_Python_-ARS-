'''

Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre
um crime. As perguntas são:

a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Devia para a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

'''

contador_sim = 0

pergunta_1 = int(input('Telefonou para a vítima? (1 - Sim / 2 - Não): '))
if pergunta_1 == 1:
    contador_sim += 1

pergunta_2 = int(input('Esteve no local do crime? (1 - Sim / 2 - Não): '))
if pergunta_2 == 1:
    contador_sim += 1

pergunta_3 = int(input('Mora perto da vítima? (1 - Sim / 2 - Não): '))
if pergunta_3 == 1:
    contador_sim += 1

pergunta_4 = int(input('Devia para a vítima? (1 - Sim / 2 - Não): '))
if pergunta_4 == 1:
    contador_sim += 1

pergunta_5 = int(input('Já trabalhou com a vítima? (1 - Sim / 2 - Não): '))
if pergunta_5 == 1:
    contador_sim += 1

if contador_sim == 2:
    print('Suspeita')

elif 3 <= contador_sim <= 4:
    print('Cúmplice')

elif contador_sim == 5:
    print('Assassino')
    
else:
    print('Inocente')
