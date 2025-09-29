def escolher_opcao():
    print('Escolha a opção:\n'
          '1 - Venda à Vista\n'
          '2 - Venda a Prazo 30 dias\n'
          '3 - Venda a Prazo 60 dias\n'
          '4 - Venda a Prazo com 90 dias\n'
          '5 - Venda com cartão de débito\n'
          '6 - Venda com cartão de crédito')
    try:
        return int(input("Digite o número da opção desejada: "))
    except ValueError:
        return None

def verificacao(opcao):
    opcoes = {
        1: 'Venda à Vista',
        2: 'Venda a Prazo 30 dias',
        3: 'Venda a Prazo 60 dias',
        4: 'Venda a Prazo com 90 dias',
        5: 'Venda com cartão de débito',
        6: 'Venda com cartão de crédito'
    }
    print(opcoes.get(opcao, "Opção inválida"))

op = escolher_opcao()
verificacao(op)