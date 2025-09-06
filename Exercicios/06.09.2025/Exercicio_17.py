from math import hypot

cateto_oposto = int(input('Informe o cateto oposto: '))

cateto_adjacente = int(input('Informe o cateto adjacente: '))

hipostenusa = hypot(cateto_oposto, cateto_adjacente)  # H² = C² + C² // H² = (C² + C²) ** (1/2)

print(f'Hipotenusa: {hipostenusa}')