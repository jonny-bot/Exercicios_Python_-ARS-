import random
import statistics

def gerar_numero():
    return random.randint(1,10)

dados = []

while True:

    contador = 0

    total_numero = int(input('Digite o Total de Números a ser Gerados: '))

    while contador < total_numero:

        numero = gerar_numero()
        contador += 1
        dados.append(numero)

    if dados:
        media = statistics.mean(dados)
        mediana = statistics.median(dados)
        modas = statistics.multimode(dados)

        print("\nResumo Estatístico")
        print(f'{dados}')
        print(f"Média: {media:.2f}")
        print(f"Mediana: {mediana}")
        print(f"Moda(s): {modas}")
        break

    else:
        print("Nenhum número foi digitado.")
