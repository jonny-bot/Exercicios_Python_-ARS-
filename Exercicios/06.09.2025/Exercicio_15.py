dia_alugado = int(input('Dias alugado: '))
km_rodados = int(input('Km rodados: '))

valor = (dia_alugado * 60) + (km_rodados * 0.15)

print(f'Total a pagar: R${valor:.2f}')

