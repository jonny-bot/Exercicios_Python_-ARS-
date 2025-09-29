'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''

print("=== CALCULADORA DE PAGAMENTO ===")
preco = float(input("Digite o preço do produto: R$ "))

print("\nFormas de pagamento:")
print("1 - À vista (dinheiro/cheque) - 10% de desconto")
print("2 - À vista no cartão - 5% de desconto")
print("3 - Em até 2x no cartão - sem juros")
print("4 - Em 3x ou mais no cartão - 20% de juros")

opcao = int(input("\nEscolha a opção de pagamento (1 a 4): "))

if opcao == 1:
    total = preco * 0.90
    print(f"Pagamento à vista com 10% de desconto: R$ {total:.2f}")

elif opcao == 2:
    total = preco * 0.95
    print(f"Pagamento à vista no cartão com 5% de desconto: R$ {total:.2f}")

elif opcao == 3:
    parcela = preco / 2
    print(f"Pagamento em 2x sem juros: 2x de R$ {parcela:.2f} (Total: R$ {preco:.2f})")

elif opcao == 4:
    parcelas = int(input("Quantas parcelas? (mínimo 3): "))
    if parcelas < 3:
        print("Número de parcelas inválido. Deve ser 3 ou mais.")
    else:
        total = preco * 1.20
        valor_parcela = total / parcelas
        print(f"Pagamento com 20% de juros: {parcelas}x de R$ {valor_parcela:.2f} (Total: R$ {total:.2f})")

else:
    print("Opção inválida. Tente novamente.")
