texto = "aeiouu"
vogais = "aeiouAEIOU"
total_vogais = 0

for vogal in vogais:
    total_vogais += texto.count(vogal)

print(f"O texto tem {total_vogais} vogais.")