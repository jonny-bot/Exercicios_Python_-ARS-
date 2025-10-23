import random

jogadas = 1

maquina = random.randint(1, 100)
tentativas = int(input('Vamos ter quantas tentativas: '))

while jogadas <= tentativas:
    try:
        numero = int(input('Digite um Número: '))
        if numero < 1 or numero > 100:
            print('Digite um Número Inteiro Válido')
        else:
            if numero == maquina:
                print('Parabéns, Você Acertou!!!')
                break
            elif numero > maquina:
                print('O Número que Você Digitou é Maior!!!\n'
                      f'Essa é a Jogada: {jogadas}, Faltam {tentativas - jogadas}')
                jogadas += 1
            elif numero < maquina:
                print('O Número que Você Digitou é Menor!!!\n'
                      f'Essa é a Jogada: {jogadas}, Faltam {tentativas - jogadas}')
                jogadas += 1
            if jogadas > tentativas:
                print('Que pena, Acabou as Tentativas')
    except ValueError:
        print('Digite uma Entrada Válida')

print(f"A Máquina escolheu o Número: {maquina}")