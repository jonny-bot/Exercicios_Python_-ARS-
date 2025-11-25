lista = []

while True:
    try:

        opcao = int(input('0 - Sair || 1 - Consultar || 2 - Adicionar Nomes || 3 - Mostrar Lista\n'
                          'Digite uma das Opções: '))

        if 0 <= opcao <= 3:

            if opcao == 0:
                print('Fim do Programa...')
                break

            elif opcao == 1:

                nome = input('Digite um Nome: ')

                encontrado = False
                for i in lista:
                    if i == nome:
                        encontrado = True
                        break

                if encontrado:
                    print('Está na lista!')
                else:
                    print('Não Está na Lista!')

            elif opcao == 2:

                adicionar_nome = str(input('Digite um Nome: '))

                lista.append(adicionar_nome)

                print('Nome adicionado com Sucesso!')

            elif opcao == 3:

                contagem = 0
                for i in lista:
                    contagem += 1
                    print(f'{contagem}° Registro: {i}')

        else:
            print(f'Você Digitou {opcao}, que não é 1 ou 2.')

    except ValueError:
        print('Digite Uma Entrada Válida!')