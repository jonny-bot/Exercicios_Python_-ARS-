ano = int(input('Digite o ANO: \n'))

if ano % 400 == 0 :
    print(f'O ano {ano} é BISSEXTO!!!')
elif ano % 100 == 0:
    print(f'O ano {ano} NÂO É BISSEXTO!!!')
else:
    print(f'O ano {ano} NÂO É BISSEXTO!!!')