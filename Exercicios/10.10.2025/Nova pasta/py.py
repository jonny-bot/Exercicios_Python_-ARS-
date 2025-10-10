import random

computador = random.randint(1, 100)

rodadas = 1

while True:
    try:
        print(f'Rodada {rodadas} de 5')
        numero = int(input('Digite um número (De 1 a 100): '))
        if numero > computador:
            print('O número é menor')
            rodadas += 1

        if numero < computador:
            print('O número é maior')
            rodadas += 1

            if rodadas == 5:
                print(f'Você perdeu! O número era {computador}')
                beak
        
        if numero == computador:
            print('Parabéns, você acertou!')
            brea

    except ValueError:
        print('Digite um número válido!')
    