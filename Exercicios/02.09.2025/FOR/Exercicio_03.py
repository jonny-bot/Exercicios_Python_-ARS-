numero = int(input('Tabuada do: \n'))

print(f"--- Tabuada do {numero} ---")

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} * {i} = {resultado}')