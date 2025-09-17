'''

Caractere: vogal maiúscula
Leia um único caractere. Imprima “Vogal maiúscula”, “Vogal minúscula”, “Consoante” ou “Outro” (use in com tuplas e isalpha()).

'''

caractere = input("Digite um único caractere: ")

vogais_maiusculas = ('A', 'E', 'I', 'O', 'U')
vogais_minusculas = ('a', 'e', 'i', 'o', 'u')

if len(caractere) == 1 and caractere.isalpha():
    if caractere in vogais_maiusculas:
        print("Vogal maiúscula")
    elif caractere in vogais_minusculas:
        print("Vogal minúscula")
    else:
        print("Consoante")
else:
    print("Outro")
