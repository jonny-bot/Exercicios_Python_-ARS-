from time import sleep

time = int(input('Vamos contar até quanto: '))

i = 1

while True:
    print(i)
    sleep(0.3)
    i += 1

    if i == time:
        break

print('Fim do programa!!!')