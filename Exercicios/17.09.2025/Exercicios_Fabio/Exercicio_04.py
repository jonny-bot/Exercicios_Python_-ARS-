'''

Senha aceitável
Leia uma senha. Ela é válida se len(senha) >= 8 e contém pelo menos uma letra e um dígito (use qualquer checagem simples). Imprima “OK” ou “Fraca”.

'''

senha = input('Digite a Senha: ')

letra = False

numero = False

tamanho = len(senha)

if tamanho >= 8 :

    for i in senha:
        if i.isalpha():
            letra = True
        elif i.isdigit():
            numero = True

    if letra and numero:
        print("A senha contém letras e números.")
    else:
        print("A senha não contém letras e números.")

else:
    print('Senha Fraca')