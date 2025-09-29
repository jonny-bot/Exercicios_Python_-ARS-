def imc(peso, altura):
    return peso / (altura * altura)

def calculo_imc():
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    resultado = imc(peso, altura)
    print(f'Seu IMC é: {resultado:.2f}')
    return resultado

def classificar_imc(imc_valor):
    if imc_valor < 18.5:
        print('Classificação: Magreza (Grau 0)')

    elif imc_valor <= 24.9:
        print('Classificação: Normal (Grau 0)')

    elif imc_valor <= 29.9:
        print('Classificação: Sobrepeso (Grau I)')

    elif imc_valor <= 39.9:
        print('Classificação: Obesidade (Grau II)')

    else:
        print('Classificação: Obesidade Grave (Grau III)')

imc_resultado = calculo_imc()
classificar_imc(imc_resultado)