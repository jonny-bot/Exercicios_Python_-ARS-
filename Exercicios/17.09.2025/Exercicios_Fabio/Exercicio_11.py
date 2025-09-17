# Validação de entrada (ignorar valores negativos)

while True:
    i = int(input('Digite um Número: '))

    if i < 0: # Ignora os Números Negativos
        print(f'Número negativos ignorados')
        continue

    if i == 0: # Quando apertar o 0, ele termina o programa
        print('Encerrando!!!')
        break