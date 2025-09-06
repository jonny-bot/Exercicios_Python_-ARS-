velocidade = int(input('Informe a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado.')

    multa = (velocidade - 80) * 7.00
    print(f'Você vai pagar R$ {multa:.2f} de multa.'.format())