import random

def gerar_jogo():
    # Lista dos números mais sorteados na Mega da Virada (histórico até 2025)
    # Fonte: Caixa Econômica Federal e levantamentos
    mais_sorteados = [10, 5, 23, 33, 36, 42, 43, 51, 53, 58]

    # Gerar 6 números aleatórios entre 1 e 60
    aleatorios = random.sample(range(1, 61), 6)

    # Combinar: 3 números aleatórios + 3 dos mais sorteados
    jogo = random.sample(mais_sorteados, 3) + random.sample(aleatorios, 3)

    # Ordenar para ficar como um volante oficial
    jogo.sort()
    return jogo

# Gerar 5 palpites
for i in range(5):
    print(f"Jogo {i+1}: {gerar_jogo()}")

