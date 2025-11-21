import random

def pedra_papel_tesoura():
    lista = ['Pedra', 'Papel', 'Tesoura']
    return random.choice(lista)

while True:
    try:
        escolha_jogador = int(input('0 - Sair do Programa\n'
                                    '1 - Pedra\n'
                                    '2 - Papel\n'
                                    '3 - Tesoura\n'
                                    'Digite uma Opção: '))

        if escolha_jogador == 0:
            print("Saindo do programa")
            break

        if 1 <= escolha_jogador <= 3:

            if escolha_jogador == 1:
                escolha_jogador = 'Pedra'

            elif escolha_jogador == 2:
                escolha_jogador = 'Papel'

            else:
                escolha_jogador = 'Tesoura'

            escolha_maquina = pedra_papel_tesoura()

            print(f"Você escolheu {escolha_jogador}, a máquina escolheu {escolha_maquina}.")

            if (escolha_jogador == 'Pedra' and escolha_maquina == 'Tesoura') \
                    or (escolha_jogador == 'Papel' and escolha_maquina == 'Pedra') \
                    or (escolha_jogador == 'Tesoura' and escolha_maquina == 'Papel'):
                print('Parabéns. Você Venceu!!!')

            elif escolha_jogador == escolha_maquina:
                print('Deu Embate!!!')

            else:
                print('A Máquina Venceu!!!')

        else:
            print(f'Você Digitou {escolha_jogador}, que não está entre 0 e 3.')

    except ValueError:
        print('Digite uma Entrada Válida!!!')
