def tipo_triangulo(lado_1, lado_2, lado_3):
    if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):
        print('É um Triângulo!!!')

        if lado_1 == lado_2 == lado_3:
            print('Triângulo Equilátero!!!')

        elif lado_1 == lado_2 and lado_2 == lado_3 and lado_3 == lado_1:
            print('Triângulo Isósceles')

        else:
            print('Triângulo Escaleno')

    else:
        print('Não é um Triãngulo!!!')


lado_1 = int(input('Digite o 1° Lado: '))
lado_2 = int(input('Digite o 2° Lado: '))
lado_3 = int(input('Digite o 3° Lado: '))
tipo_triangulo(lado_1, lado_2, lado_3)
