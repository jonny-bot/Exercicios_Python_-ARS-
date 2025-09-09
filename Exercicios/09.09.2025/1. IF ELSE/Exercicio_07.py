a = float(input('1° lado: '))

b = float(input('2°  lado: '))

c = float(input('3° lado: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Não é um triangulo')

elif (a == b) and (a == c):
    print('Equilatero')

elif (a == b) or (a == c) or (b == c):
    print('Isósceles')

else:
    print('Escaleno')