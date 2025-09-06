numero =  int(input('Digite um Número: \n'))

if numero > 1:
    for i in range(2, numero):
        print(f'{numero} náo é primo')
        break
    else:
        print(f'{numero} é primo!')
else:
    print(f'{numero} é primo!')
