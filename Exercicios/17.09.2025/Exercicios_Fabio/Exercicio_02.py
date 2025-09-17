'''

Maioridade e CNH
Leia idade e tem_cnh ('S'/'N'). Imprima “Pode dirigir” se idade >= 18 and tem_cnh == 'S'; senão “Não pode”.


'''

idade = int(input('Digite a Idade: '))

if idade <= 17:
    print('Não Tem Idade para Dirigir!!!')
else:

    tem_CNH = input('Ele possui CNH: ').lower()
    print('Não Tem Idade para Dirigir!!!')

    if idade >= 18 and tem_CNH == 's':
        print('Pode Dirigir!!!')
    else:
        print('Não Pode Dirigir!!!')