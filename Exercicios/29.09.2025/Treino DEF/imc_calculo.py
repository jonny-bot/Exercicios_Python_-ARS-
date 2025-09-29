def imc(peso, altura):
    return peso / (altura * altura)

def calculo_imc():
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite sua altura: '))
    resultado = imc(peso, altura)
    print(f'Seu resultado da: {resultado:.2f}')
    return resultado

def classificacao_imc(class_imc):
    if class_imc < 18.5:
        print('Abaixo do Peso')
    elif class_imc <= 24.9:
        print('Peso Normal')
    elif class_imc <= 29.9:
        print('Sobrepeso')
    elif class_imc <= 34.9:
        print('Obesidade Grau I')
    elif class_imc <= 39.9:
        print('Obesidade Grau II')
    else:
        print('Obesidade Grau III')


resultado_imc = calculo_imc()
classificacao_imc(resultado_imc)