def criar_conta():
    nome = input('Digite o Nome da Conta:')

    senha = int(input('Digite a senha de 4 Dígitos: '))

    saldo_inicial = float(input('Qual o Saldo Inicial: '))

    if nome in conta:
        print('Essa conta já existe.')
    else:
        conta.append({'nome': nome, 'senha': senha, 'saldo inicial': saldo_inicial})

        print('Conta criado com sucesso!!!')
        # print(conta)


def autenticar_usuario():
    nome = input("Digite o Nome da Conta: ")
    senha = input("Digite a senha da Conta: ")

    for j in conta:
        if nome == j["nome"] and int(senha) == j["senha"]:
            print('==============================')
            print('Login realizado com Sucesso!!!')
            print('==============================')
            return

    print('======================')
    print('Login não realizado!!!')
    print('======================')

conta = []


while True:
    print('=== Caixa Eletrônico ===')
    print('1. Criar Conta')
    print('2. Fazer Login')
    print('3. Sair')

    opcao = (input('Escolha uma Opção:'))

    if opcao == '3':
        print('Saindo do Sistema...')
        break

    if opcao == '1':
        criar_conta()

    if opcao == '2':
        autenticar_usuario()

    def sacar(usuario, valor):
        for c in conta:
            if c["nome"] == usuario:
                if valor <= c["saldo"]:
                    c["saldo"] -= valor
                    print(f"Saque de R${valor} realizado com sucesso!")
                else:
                    print("Saldo insuficiente.")
                return





        while True:
            print('=== Menu ===')
            print('1. Sacar')
            print('2. Depositar')
            print('3. Transferir')
            print('4. Emitir Extrato')
            print('5. Sair')

            menu = (input('Escolha uma Opção:'))

            if menu == '5':
                print('Saindo do Sistema...')
                break