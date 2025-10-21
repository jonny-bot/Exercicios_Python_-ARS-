def antecessor_sucessor(numero):
    numero_antecessor = numero - 1
    print(numero_antecessor)

    numero_sucessor = numero + 1
    print(numero_sucessor)

    return numero_antecessor, numero_sucessor

num = 7

mostrar = antecessor_sucessor(num)
