import random

Numero_aleatorio= random.randint(1, 101)

tentativas = 7

for rodadas in range(1 , tentativas + 1):

    chute = int(input('Digite um Número entre 1 e 100: '))

    print(f'Tentativa {rodadas} de {tentativas}')

    if (chute < 1 and chute > 100):
        print('Você deve Digitar um Número entre 1 e 100!!!')
        continue

    acertou = (chute == Numero_aleatorio)
    maior = (chute > Numero_aleatorio)
    menor = (chute < Numero_aleatorio)

    if(acertou):
        print('Você acertou!!!')
        break

    else:
        if(maior):
            print("você errou! o seu chute foi maior que o numero secreto")
        else:
            print("você errou! o seu chute foi menor que o numero secreto")

print(f'O Número aleatorio escolhido pela maquina foi: {Numero_aleatorio}')
