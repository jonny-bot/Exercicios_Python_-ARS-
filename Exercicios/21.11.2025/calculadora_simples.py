numero_1 = int(input('Digite o 1° Número: '))

numero_2 = int(input('Digite o 2° Número: '))


while True:
    try:
        opcoes = int(input('0 - Sair do Programa\n'
                           '1 - Mais(+)\n'
                           '2 - Menos(-)\n'
                           '3 - Multiplicação(*)\n'
                           '4 - Divisão(/)\n'
                           'Digite umas das Opções: '))

        if opcoes == 0:
            print('Saindo do Programa!!!')
            break

        elif opcoes == 1:
            resultado = numero_1 + numero_2

            print(f'O Resultado deu: {resultado}')

        elif opcoes == 2:
            resultado = numero_1 - numero_2

            print(f'O Resultado deu: {resultado}')

        elif opcoes == 3:
            resultado = numero_1 * numero_2

            print(f'O Resultado deu: {resultado}')

        elif opcoes == 4:
            resultado = numero_1 / numero_2

            print(f'O Resultado deu: {resultado}')

        else:
            print(f'Você digitou {opcoes}. Que não está entre 0 e 4.')

    except ValueError:
        print('Digite uma Entrada Válida!!!')