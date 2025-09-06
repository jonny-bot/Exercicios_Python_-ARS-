distancia = int(input('Informe a distância em KM: '))

preco_passagem = distancia * 0.45 if distancia > 200 else distancia * 0.50

print(f'O valor da passagem será R$ {preco_passagem:.2f}'.format())