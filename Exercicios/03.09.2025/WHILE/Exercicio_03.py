import random

numero_secreto = random.randint(1, 100)  # Gera um número entre 1 e 10
chute = 0  # Inicializa o chute para que o loop seja executado

while chute != numero_secreto:
    chute = int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
    if chute < numero_secreto:
        print("Tente um número maior!")
    elif chute > numero_secreto:
        print("Tente um número menor!")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")