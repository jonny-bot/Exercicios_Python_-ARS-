import time

n = int(input("Digite um número para iniciar a contagem regressiva: "))
while n >= 1:
    print(n)
    time.sleep(1)
    n -= 1
print("Fogo!")
