
print('CALCULANDO FATORIAL\n')


numero = int(input('Digite um número inteiro: '))

resultado = 1
contador = 1

while contador <= numero:
    resultado *= contador
    print(f'Passo {contador}: {resultado}')
    contador += 1

print('\nO resultado de {}! é: {}'.format(numero, resultado))