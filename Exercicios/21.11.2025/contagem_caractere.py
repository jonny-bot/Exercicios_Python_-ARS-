texto = input('Digite uma Frase: ')

maiusculas = sum(1 for c in texto if c.isupper())
minusculas = sum(1 for c in texto if c.islower())
espacos = texto.count(" ")

print(f"Maiúsculas: {maiusculas}\n"
      f"Minusculas: {minusculas}\n"
      f"Espaços: {espacos}")
