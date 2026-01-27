def variaveis_e_tipos_de_dados():
    # Criando Variáveis
    nome = 'João'   # string
    idade = 24      # int (inteiro)
    altura = 1.75   # float (decimal)
    ativo = True    # booleanos (True ou False)

    # Imprimindo Valores
    print(altura)
    print(ativo)

    # Descobrindo o Tipo
    print(type(nome))
    print(type(idade))


def condicionais():

    # '==' - Igual
    # '!=' - Diferente
    # '<' - Menor
    # '>' - Maior
    # '<=' - Menor Igual
    # '>=' - Maior Igual

    # Básico if / else
    trabalho_terminado = True

    if trabalho_terminado == True:
        print("Bora sair!")
    else:
        print("Não posso sair agora.")

    # Múltiplas Condições if / elif / else
    atrasos = 2

    if atrasos >= 3:
        print("Você está suspenso!")
    elif atrasos == 2:
        print("Mais uma falta e será suspenso.")
    elif atrasos == 1:
        print("Mais duas faltas e será suspenso.")
    else:
        print("Pode entrar.")


def lacos_repeticao_for():
    # Imprimir de 0 a 4
    for i in range(5):
        print(i)

    # Imprimir de 1 a 10
    for i in range(1, 11):
        print(i)

    # Imprimir de 2 a 10 pulando de 2 em 2
    for i in range(2, 11, 2):
        print(i)

    # Percorrendo Lista
    nomes = ["João", "Maria", "Ana"]
    for nome in nomes:
        print(nome)

    # Lista com tipos mistos
    dados = [1, "Python", True, 2.5]
    for dado in dados:
        print(dado)

    # for + if
    idades = [13, 15, 18, 30, 50, 75]
    for idade in idades:
        if idade >= 18:
            print(f"{idade} é maior de idade")
        else:
            print(f"{idade} é menor de idade")


def lacos_repeticao_while():
    # Básico com Contador
    tentativas = 0

    while tentativas < 3:
        print("Tente novamente")
        tentativas += 1
    print("Fim das tentativas")

    # Com Senha (repetir até acertar)
    senha = ""

    while senha != "12345":
        senha = input("Digite a senha: ")
    print("Bem-vindo ao sistema!")

    # Validação de Entrada
    nome = ""

    while nome == "":
        nome = input("Digite seu nome: ")
    print(f"Bem-vindo, {nome}!")


def listas():
    # Criando listas
    numeros = [10, 20, 30]
    nomes = ["João", "Pedro", "Marta"]
    mistura = [1, "Python", True, 2.5]

    # Acessando elementos
    print(numeros[0])  # 10
    print(nomes[-1])  # Marta
    print(mistura)

    # Descobrindo o índice
    print(nomes.index("João"))  # 1

    # Adicionando elementos
    numeros.append(40)
    print(numeros)  # [10, 20, 30, 40]

    # Percorrendo uma lista
    for nome in nomes:
        print(nome)

    # Soma de Valores de uma Lista
    salarios = [2500, 900, 5000, 7500]

    total = 0

    for salario in salarios:
        total += salario
    print(f"Total pago: {total}")


while True:
    try:

        opcoes = {

            0:'Sair do Programa',

            1:'variaveis_e_tipos_de_dados()',

            2:'condicionais()',

            3:'lacos_repeticao_for()',

            4:'lacos_repeticao_while()',

            5:'lista()'

        }

        print("=== MENU DE OPÇÕES ===")
        for chave, valor in opcoes.items():
            print(f"{chave} - {valor}")

        escolha = int(input('Digite umas das Escolhas: '))

        match escolha:

            case 0:
                print('Fim do Programa!')
                break

            case 1:
                variaveis_e_tipos_de_dados()

            case 2:
                condicionais()

            case 3:
                lacos_repeticao_for()

            case 4:
                lacos_repeticao_while()

            case 5:
                listas()

    except ValueError:
        print('Digite uma Entrada Válida!')
