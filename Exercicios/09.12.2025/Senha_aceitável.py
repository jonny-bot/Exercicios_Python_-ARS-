'''

Senha aceitável
Leia uma senha.
Ela é válida se len(senha) >= 8 e contém pelo menos uma letra e um dígito
(use qualquer checagem simples).
Imprima “OK” ou “Fraca”.

'''

print("Cadastre aqui sua senha com os seguintes criétios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
senha = str(input("Digite sua senha : "))

while senha.islower():
        senha = input("A senha deve ter pelo menos um caractere MAIUSCULO: ")

while len(senha) < 7 :
    senha = input("A senha deve ter pelo menos 8 caracteres: ")

while senha.isalpha() :
    senha = input("Necessita de um numero: ")

while senha.isalnum() :
    senha = input("Necessita de um Caractere especial: ")
