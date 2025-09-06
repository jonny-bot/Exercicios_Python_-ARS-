# contar quantas vogais tem em uma frase

frase = input('Digite uma fráse: ')

contador_vogais = 0

for var in frase:

    if var.lower() in 'aeiou':
        contador_vogais += 1

print(f'A frase é {frase} e contem {contador_vogais} vogais!!!')