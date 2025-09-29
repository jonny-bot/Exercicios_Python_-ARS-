import random
import time


# Crie um programa que faça o computador jogar Jokenpô com você.


import random
import time

# Opções disponíveis
choices_list = ["pedra", "papel", "tesoura"]

# Introdução
print("""
🎮 BEM-VINDO AO JOKENPÔ COM PONTUAÇÃO 🎮
Regras:
- Pedra vence Tesoura
- Tesoura vence Papel
- Papel vence Pedra
""")

rodadas = int(input("Quantas rodadas você quer jogar? "))
player_score = 0
computer_score = 0

for rodada in range(1, rodadas + 1):
    print(f"\n🕹️ Rodada {rodada} de {rodadas}")
    player_choice = input("Escolha pedra, papel ou tesoura: ").lower()

    if player_choice not in choices_list:
        print("Escolha inválida! Você perdeu esta rodada.")
        computer_score += 1
        continue

    computer_choice = random.choice(choices_list)

    print("JO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PÔ!!!")

    print(f"\nVocê escolheu: {player_choice}")
    print(f"Computador escolheu: {computer_choice}")

    if player_choice == computer_choice:
        print("Empate!")
    elif (player_choice == "pedra" and computer_choice == "tesoura") or \
         (player_choice == "papel" and computer_choice == "pedra") or \
         (player_choice == "tesoura" and computer_choice == "papel"):
        print("Você venceu esta rodada! 🎉")
        player_score += 1
    else:
        print("Computador venceu esta rodada! 💻")
        computer_score += 1

# Resultado final
print("\n🏁 FIM DE JOGO 🏁")
print(f"Placar final: Você {player_score} x {computer_score} Computador")

if player_score > computer_score:
    print("🎊 Parabéns! Você venceu o jogo!")
elif player_score < computer_score:
    print("😢 O computador venceu o jogo. Tente novamente!")
else:
    print("🤝 Empate geral! Boa partida!")