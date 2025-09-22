# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('M-matutino ou V-Vespertino ou N- Noturno')

opcoes = ['M', 'V', 'N']

turno = []

while turno != opcoes:

    turno = input('Qual turno você estuda: ').lower()

    if turno == 'm':
        print('Bom Dia!!!')
        break
    elif turno == 'v':
        print('Boa Tarde!!!')
        break
    elif turno == 'n':
        print('Boa Noite!!!')
        break
    else:
        print('Valor Inválido!')