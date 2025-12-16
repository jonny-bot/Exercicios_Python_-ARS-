import random

palavras = ["casa", "carro", "livro", "python", "termo"]
palavra_secreta = random.choice(palavras)

tentativas = 6
while tentativas > 0:

    chute = input("Digite uma palavra: ").lower()

    if chute == palavra_secreta:
        print("Você acertou!")
        break

    else:
        dica = "".join([c if c == palavra_secreta[i] else "_" for i, c in enumerate(chute)])
        print("Dica:", dica)
        tentativas -= 1

if tentativas == 0:
    print(f"Fim de jogo. A palavra era: {palavra_secreta}")
