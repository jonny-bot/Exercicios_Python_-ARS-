
senha = str(input('Digite a sua senha: '))

while senha.islower():
    senha = input('A senha deve ter uma Letra Maiúscula:')

while len(senha) < 7:
    senha = input('A senha deve conter no Minimo 8 caracteres: ')

while senha.isalpha():
    senha = input('A senha deve conter Números: ')

while senha.isalnum():
    senha = input('A senha precisa de uma caractere especial:')

print('Senha Validada!!!')