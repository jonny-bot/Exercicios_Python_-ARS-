# Faça um Programa que peça um número correspondente a um determinado
# ano e em seguida informe se este ano é ou não bissexto.

'''

Regras para determinar um ano bissexto:

Se o ano não termina em "00": Verifique se o número é divisível por 4.
    Exemplo: 2024 é bissexto porque 24 é divisível por 4. 1998 não é bissexto, pois 98 não é divisível por 4.
Se o ano termina em "00": Verifique se o número é divisível por 400.
    Exemplo: 2000 foi um ano bissexto porque é divisível por 400. 1900 não foi um ano bissexto, pois não é divisível por 400.

'''

ano = 1900

# ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")