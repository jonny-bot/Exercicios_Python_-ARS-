'''

Desfio: Jogo da Senha (Mastermind Simples)

O computador gera uma sequência aleatorio de 4 numeros (de 1 a 6, podendo repetir).
Você deve tentar descobrir a sequência em até 10 tentativas.
A cada tentativa, o programa informa:

    - Quantos números você acertou na posição certa.
    - Quantos números acertou, mas estão em posição errada.

Regras:

    - Use apenas Python puro (Sem biblioteca Externa).
    - As dicas (quantos acertos na posição e fora da posição) são mostradas a cada jogada.
    - Quantos acertar tudo, mostre parabéns e o números de tentativas.
    - Se não acertar em 10 tentativas, mostrar se nha correta.

'''

import random

def gerar_senha():
    """Gera uma senha aleatória com 4 números entre 1 e 6 (com repetição)."""
    return [random.randint(1, 6) for _ in range(4)]

def avaliar_tentativa(senha, tentativa):
    """Avalia a tentativa do jogador comparando com a senha."""
    certos_posicao = 0
    certos_fora = 0

    senha_temp = senha.copy()
    tentativa_temp = tentativa.copy()

    # Verifica acertos na posição correta
    for i in range(4):
        if tentativa_temp[i] == senha_temp[i]:
            certos_posicao += 1
            senha_temp[i] = tentativa_temp[i] = None

    # Verifica acertos fora da posição
    for i in range(4):
        if tentativa_temp[i] is not None and tentativa_temp[i] in senha_temp:
            certos_fora += 1
            idx = senha_temp.index(tentativa_temp[i])
            senha_temp[idx] = None

    return certos_posicao, certos_fora

def obter_tentativa(numero):
    """Solicita uma tentativa válida ao jogador."""
    while True:
        entrada = input(f"Tentativa {numero}: Digite 4 números entre 1 e 6 separados por espaço: ")
        partes = entrada.strip().split()
        if len(partes) == 4 and all(p.isdigit() and 1 <= int(p) <= 6 for p in partes):
            return [int(p) for p in partes]
        else:
            print("❌ Entrada inválida! Digite exatamente 4 números entre 1 e 6.")

def main():
    senha = gerar_senha()
    tentativas_max = 10

    print("🔐 Bem-vindo ao Jogo da Senha (Mastermind Simples)!")
    print("Descubra a sequência de 4 números entre 1 e 6 (pode repetir).")
    print("Você tem até 10 tentativas. Boa sorte!\n")

    for tentativa_num in range(1, tentativas_max + 1):
        tentativa = obter_tentativa(tentativa_num)
        certos_pos, certos_fora = avaliar_tentativa(senha, tentativa)

        print(f"🎯 {certos_pos} número(s) na posição certa.")
        print(f"🔄 {certos_fora} número(s) certo(s), mas em posição errada.\n")

        if certos_pos == 4:
            print(f"🎉 Parabéns! Você descobriu a senha em {tentativa_num} tentativa(s)!")
            break
    else:
        print(f"😢 Que pena! Você não acertou. A senha correta era: {senha}")

if __name__ == "__main__":
    main()