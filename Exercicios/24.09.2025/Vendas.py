valor = float(input('Qual o valor do Produto: '))

lista = [print('Escolha a opcao: \n'
               '1-Venda a Vista \n'
               '2-Venda a Prazo 30 dias \n'
               '3-Venda a Prazo 60 dias \n'
               '4-Venda a Prazo com 90 dias \n'
               '5-Venda com cartao de debito \n'
               '6-Venda com cartao de credito')
]

opcao = int(input("Digite a opcao:"))

if opcao == 1:
    print('1-Venda a Vista')
    valor_final = valor * 0.90

elif opcao == 2:
    print('2-Venda a Prazo 30 dias')
    valor_final = valor * 1.10

elif opcao == 3:
    print('3-Venda a Prazo 60 dias')
    valor_final = valor * 1.15

elif opcao == 4:
    print('4-Venda a Prazo com 90 dias')
    valor_final = valor * 1.20

elif opcao == 5:
    print('5-Venda com cartao de debito')
    valor_final = valor * 1.05

elif opcao == 6:
    print('6-Venda com cartao de credito')
    parcelas = int(input('Vai ser Dividido em quantas parcelas: '))
    valor_final = valor * 1.05
    print(f"Valor por parcela: {valor_final / parcelas:.2f}")
else:
    print("Opcao invalida")
    valor_final = None

if valor_final:
    print(f"Valor final da compra: R$ {valor_final:.2f}")