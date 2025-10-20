import random
print("*******************************")
print("Bem vindo ao Termo")
print("*******************************")

vocabulario = ["feliz","dados","furia","treta","pombo","drama"]
palavra = random.choice(vocabulario)

chances = 5
alfabeto = list("abcdefghijklmnopqrstuvwxyz")
tentativas = []

while True:
    print(tentativas)
    print("Chances: ", chances)

    for letra in palavra:
        if letra in tentativas:
            print(letra, end='')
        else:
                print('_', end='')
    palpite = input("\nDigite seu palpite ou 'SAIR' para sair do programa!").lower()
    if palpite == "sair":
        break
    elif palpite not in alfabeto or palpite == '':
        print("Hein!? Fala direito! Isso não é uma letra!")
        continue
    elif palpite in tentativas:
        print("Você é desmemoriado ou o quê!? Você já tentou essa letra. Tente outra!")
        continue
    tentativas.append(palpite)
    if palpite in palavra:
        print("ACERTÔ, MIZERAVI")
    else:
        print("Errou feio, errou rude!")
        chances -= 1
    if chances == 0:
        print("Perdeu, pivete! Game over!!! >:)")
        break
    elif set(palavra).issubset(set(tentativas)):
        print("Parabéns, você acertou! Weeee are the champions, my frieeeend!")
        break