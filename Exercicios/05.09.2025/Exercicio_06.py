texto = "joao victor segato bonifacio 3103"

vogais = 0

consoantes = 0

digitos = 0

espacos = 0

vogais_lista = "aeiou"

texto = texto.lower() # Converte para minúsculas

for ch in texto:
    if ch in vogais_lista: # variável de vogal
        vogais += 1
    elif ch.isspace(): # Verificar quantos espaços
        espacos += 1
    elif ch.isdigit(): # Verificar quantos digitos tem
        digitos += 1
    elif ch.isalpha(): # Verifica se é uma letra é uma consoante não uma vogal
        consoantes += 1

print(f"Texto: {texto}")

print(f"Número de vogais: {vogais}")

print(f"Número de consoantes: {consoantes}")

print(f"Número de dígitos: {digitos}")

print(f"Número de espaços: {espacos}")