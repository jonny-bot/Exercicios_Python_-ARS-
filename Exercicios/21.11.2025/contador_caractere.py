frase = 'Olá Mundo'

for i in frase:
    # Exibindo o caractere e os testes de classificação
    print(f"Caractere: '{i}'")
    print(f"É letra?   {i.isalpha()}") # Verifica se o caractere é uma letra (A-Z, a-z, incluindo acentos)
    print(f"É dígito?  {i.isdigit()}") # Verifica se o caractere é um número (0-9)
    print(f"É espaço?  {i.isspace()}") # Verifica se o caractere é um espaço em branco
    print("-" * 20)
