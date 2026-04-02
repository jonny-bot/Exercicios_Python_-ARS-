def tabuada_for():
    tabuada = 0
    for i in range(1, (10 + 1)):
        tabuada += 1
        print(f'===== {tabuada} =====')
        for j in range(1, (10 + 1)):
            resultado = i * j
            print(f'{i} X {j} = {resultado}')

def tabuada_while():
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            resultado = i * j
            print(f'{i} X {j} = {resultado}')
            j += 1
        i += 1

tabuada_while()
