while True:
    try:
        alternativa_escolhida = int(input('Digite a alternativa correta: '))
        if alternativa_escolhida not in (1,2,3,4):
            print("Digite uma entrada Válida")
    except ValueError:
        print("Erro: por favor, digite um número inteiro válido.")
