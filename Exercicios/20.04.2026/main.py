import random as rn


def numero_gerado():
    return rn.randint(1, 100)


def jogar():
    
    total_tentativas = int(input("Digite o número de tentativas que deseja: "))
    numero = numero_gerado()

    contador = 0

    while contador < total_tentativas:
        try:
            print(f"Tentativa {contador+1}/{total_tentativas}")
            adivinha = int(input("Digite sua adivinha (1 a 100): "))

            if adivinha < numero:
                print("Muito baixo! Tente novamente.")

            elif adivinha > numero:
                print("Muito alto! Tente novamente.")

            else:
                print(f"🎉 Parabéns! Você adivinhou o número {numero} em {contador+1} tentativas!")
                return

            contador += 1

        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")

    print(f"Suas tentativas acabaram! O número era {numero}.")


def main():
    while True:
        jogar()
        repetir = input("Deseja jogar novamente? (s/n): ").lower()
        if repetir != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":    
    main()
