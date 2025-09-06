import random

def jogar_pedra_papel_tesoura():

    opcoes = ["pedra", "papel", "tesoura"]
    pontos_computador = 0
    pontos_jogador = 0
    pontos_para_vencer = 3

    print("Bem-vindo ao Pedra, Papel e Tesoura!\n")
    print(f"O primeiro a atingir {pontos_para_vencer} pontos vence!\n")


    while pontos_computador < pontos_para_vencer and pontos_jogador < pontos_para_vencer:
        print(f"--- Placar: Computador {pontos_computador} x {pontos_jogador} Jogador ---\n")


        while True:
            escolha_jogador = input("Escolha: pedra, papel ou tesoura? ").lower()
            if escolha_jogador in opcoes:
                break
            else:
                print("Opção inválida! Por favor, insira 'pedra', 'papel' ou 'tesoura'.")


        escolha_computador = random.choice(opcoes)
        print(f"O computador escolheu: {escolha_computador}\n")


        if escolha_jogador == escolha_computador:
            print("Empate!")
        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
             (escolha_jogador == "tesoura" and escolha_computador == "papel") or \
             (escolha_jogador == "papel" and escolha_computador == "pedra"):
            print("Você ganhou a rodada!")
            pontos_jogador += 1
        else:
            print("O computador ganhou a rodada!")
            pontos_computador += 1

        print("-" * 20)


    if pontos_jogador > pontos_computador:
        print("\nParabéns! Você venceu o jogo!\n")
    else:
        print("\nO computador venceu o jogo!\n")

jogar_pedra_papel_tesoura()