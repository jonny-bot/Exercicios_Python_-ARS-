'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''
lado_a = float(input("Primeiro segmento de reta: \n"))
lado_b = float(input("Segundo segmento de reta: \n"))
lado_c = float(input("Terceiro segmento de reta: \n"))

if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    print("O triângulo que existe é um ", end="")
    if lado_a == lado_b == lado_c:
        print("triângulo EQUILÁTERO.")
    elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c):
        print("triângulo ISÓSCELES.")
    else:
        print("triângulo ESCALENO.")
else:
    print("O triângulo inexiste.")