class Conta:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self._senha = senha
        self._saldo = 0.0
        self._extrato = []

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return
        self._saldo += valor
        self._extrato.append(f"Depósito: +R${valor:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return
        if valor > self._saldo:
            print("Saldo insuficiente.")
            return
        self._saldo -= valor
        self._extrato.append(f"Saque: -R${valor:.2f}")

    def transferir(self, destino, valor):
        if valor <= 0:
            print("Valor inválido.")
            return
        if valor > self._saldo:
            print("Saldo insuficiente.")
            return
        self._saldo -= valor
        destino._saldo += valor
        self._extrato.append(f"Transferência para {destino.usuario}: -R${valor:.2f}")
        destino._extrato.append(f"Transferência de {self.usuario}: +R${valor:.2f}")

    def emitir_extrato(self):
        print(f"\nExtrato de {self.usuario}:")
        for item in self._extrato:
            print(f"  {item}")
        print(f"Saldo atual: R${self._saldo:.2f}\n")

    def autenticar(self, senha):
        return self._senha == senha


class Banco:
    def __init__(self):
        self._contas = {}

    def criar_conta(self, usuario, senha):
        if usuario in self._contas:
            print("Usuário já existe.")
        else:
            self._contas[usuario] = Conta(usuario, senha)
            print("Conta criada com sucesso!")

    def autenticar(self, usuario, senha):
        conta = self._contas.get(usuario)
        if conta and conta.autenticar(senha):
            print(f"Bem-vindo, {usuario}!")
            return conta
        else:
            print("Usuário ou senha incorretos.")
            return None

    def obter_conta(self, usuario):
        return self._contas.get(usuario)


def menu_principal():
    banco = Banco()
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Criar conta")
        print("2. Login")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            usuario = input("Nome de usuário: ")
            senha = input("Senha: ")
            banco.criar_conta(usuario, senha)

        elif escolha == "2":
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            conta = banco.autenticar(usuario, senha)
            if conta:
                menu_conta(conta, banco)

        elif escolha == "3":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")


def menu_conta(conta, banco):
    while True:
        print(f"\n--- MENU DE {conta.usuario.upper()} ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Transferir")
        print("4. Emitir extrato")
        print("5. Logout")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            valor = float(input("Valor para depósito: R$"))
            conta.depositar(valor)

        elif escolha == "2":
            valor = float(input("Valor para saque: R$"))
            conta.sacar(valor)

        elif escolha == "3":
            destino_usuario = input("Usuário de destino: ")
            destino = banco.obter_conta(destino_usuario)
            if destino:
                valor = float(input("Valor para transferência: R$"))
                conta.transferir(destino, valor)
            else:
                print("Conta de destino não encontrada.")

        elif escolha == "4":
            conta.emitir_extrato()

        elif escolha == "5":
            print("Logout realizado.")
            break

        else:
            print("Opção inválida.")


# Iniciar o programa
menu_principal()
