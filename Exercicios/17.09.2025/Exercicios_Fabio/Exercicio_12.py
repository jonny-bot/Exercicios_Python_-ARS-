# Somar números ímpares até que o usuário digite 0

soma = 0

while True:
    i = int(input('Digite um Número: '))

    if i == 0:
        print('Encerrado')
        break

    if i % 2 == 0:
        continue
    soma += i
print(soma)