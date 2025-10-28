import random

print('1 - D4 || 2 - D6 || 3 - D8 || 4 - D10 || 5 - D12 || 6 - D20 || 7 - D100')

dados = {
    1: 4,
    2: 6,
    3: 8,
    4: 10,
    5: 12,
    6: 20,
    7: 100
}

while True:
    try:
        tipo_dado = int(input("Digite o Tipo de Dado: "))
        if tipo_dado in dados:
            vezes = int(input("Quantas vezes deseja jogar o dado? "))
            print(f'\nJogando um D{dados[tipo_dado]} {vezes} vez(es):')
            for i in range(vezes):
                dado = random.randint(1, dados[tipo_dado])
                print(f'Jogada {i+1}: {dado}')
            break
        else:
            print('Digite um número entre 1 e 7!')
    except ValueError:
        print('Digite uma entrada válida!')
