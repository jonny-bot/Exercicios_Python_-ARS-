import random

numero_maquina = random.randint(1 , 101)

numero_jogado = int(input('Digite um Número: '))

if (numero_jogado == numero_maquina):
    print('Parabens!!! Você acertou!!!')
else:
    print('Que pena!!! Você errou!!!')

    

print(f"O Número que você escolheu foi o {numero_jogado} e o Número escolido pela maquina é: {numero_maquina}")
