frase = input('Digite uma frase: ').strip()

print('Quantas vezes a letra "A" apareceu: ', frase.upper().count('A'))

print('Ela aparece a primeira vez na posição: ', frase.upper().find('A') + 1)

print('Ela aparece a ultima vez na posição: ', frase.upper().rfind('A') + 1)