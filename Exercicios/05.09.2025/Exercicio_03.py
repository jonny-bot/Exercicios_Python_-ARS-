import random

lista = ['joao', 'Natália', 'Pedro']

maquina = random.randint(lista)

jogador = input('Digite um nome: ').lower()

if jogador != lista:
    print('Você não advinhou o nome!!!')
else:
    print('Você advinhou o nome!!!')