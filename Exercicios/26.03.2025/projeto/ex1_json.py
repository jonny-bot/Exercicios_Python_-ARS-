import json

def exercicios_json():
    # abrir local do arquivo || 'r' = somente leitura
    with open('Exercicios_JSON/exercicio1.json', 'r', encoding='utf-8') as xyz:
        usuarios = json.load(xyz)

    for i in usuarios:

        print(i['nome'],
              i['idade'],
              i['homem'],
              i['peso'],
              i['altura'])

def imc_de_todos():

    # abrir local do arquivo || 'r' = somente leitura
    with open('Exercicios_JSON/exercicio1.json', 'r', encoding='utf-8') as xyz:
        usuarios = json.load(xyz)

    for i in usuarios:

        nome = i['nome']
        idade = i['idade']
        homem = i['homem']
        peso = i['peso']
        altura = i['altura']

        imc = peso / (altura ** 2)

        if imc <= 18.5:
            print(f'{nome} tem {imc:.2f} e está a baixo')
        elif imc <= 25:
            print(f'{nome} tem {imc:.2f} e está a normal')
        else:
            print(f'{nome} tem {imc:.2f} e está a sobre peso')

def imc_homem():

    # abrir local do arquivo || 'r' = somente leitura
    with open('Exercicios_JSON/exercicio1.json', 'r', encoding='utf-8') as xyz:
        usuarios = json.load(xyz)

    for i in usuarios:

        nome = i['nome']
        idade = i['idade']
        homem = i['homem']
        peso = i['peso']
        altura = i['altura']

        imc = peso / (altura ** 2)

        if homem == True:
            if imc <= 18.5:
                print(f'{nome} tem {imc:.2f} e está a baixo')
            elif imc <= 25:
                print(f'{nome} tem {imc:.2f} e está a normal')
            else:
                print(f'{nome} tem {imc:.2f} e está a sobre peso')

def imc_mulher():
    # abrir local do arquivo || 'r' = somente leitura
    with open('Exercicios_JSON/exercicio1.json', 'r', encoding='utf-8') as xyz:
        usuarios = json.load(xyz)

    for i in usuarios:

        nome = i['nome']
        idade = i['idade']
        homem = i['homem']
        peso = i['peso']
        altura = i['altura']

        imc = peso / (altura ** 2)

        if homem == False:
            if imc <= 18.5:
                print(f'{nome} tem {imc:.2f} e está a baixo')
            elif imc <= 25:
                print(f'{nome} tem {imc:.2f} e está a normal')
            else:
                print(f'{nome} tem {imc:.2f} e está a sobre peso')

def media_imc_homem():
    # abrir local do arquivo || 'r' = somente leitura
    with open('Exercicios_JSON/exercicio1.json', 'r', encoding='utf-8') as xyz:
        usuarios = json.load(xyz)

    contador = 0
    somatoria_imc = 0

    for i in usuarios:

        nome = i['nome']
        idade = i['idade']
        homem = i['homem']
        peso = i['peso']
        altura = i['altura']

        imc = peso / (altura ** 2)

        if homem == True:
            if imc <= 18.5:
                print(f'{nome} tem {imc:.2f} e está a baixo')
            elif imc <= 25:
                print(f'{nome} tem {imc:.2f} e está a normal')
            else:
                print(f'{nome} tem {imc:.2f} e está a sobre peso')
            contador += 1
            somatoria_imc += imc

    media = somatoria_imc / contador

    print(f'A média de IMC dos Homens é de: {media:.2f}')

def media_imc_mulher():
    # abrir local do arquivo || 'r' = somente leitura
    with open('Exercicios_JSON/exercicio1.json', 'r', encoding='utf-8') as xyz:
        usuarios = json.load(xyz)

    contador = 0
    somatoria_imc = 0

    for i in usuarios:

        nome = i['nome']
        idade = i['idade']
        homem = i['homem']
        peso = i['peso']
        altura = i['altura']

        imc = peso / (altura ** 2)

        if homem == False:
            if imc <= 18.5:
                print(f'{nome} tem {imc:.2f} e está a baixo')
            elif imc <= 25:
                print(f'{nome} tem {imc:.2f} e está a normal')
            else:
                print(f'{nome} tem {imc:.2f} e está a sobre peso')
            contador += 1
            somatoria_imc += imc

    media = somatoria_imc / contador

    print(f'A média de IMC dos Homens é de: {media:.2f}')

def pessoa_alta_baixa():

    with open('Exercicios_JSON/exercicio1.json', 'r', encoding='utf-8') as xyz:
        usuarios = json.load(xyz)

    mais_alta = 0
    nome_mais_alto = ""

    mais_baixa = usuarios[0]['altura']
    nome_mais_baixo = usuarios[0]['nome']

    for i in usuarios:
        if i['altura'] < mais_baixa:
            mais_baixa = i['altura']
            nome_mais_baixo = i['nome']

        if i['altura'] > mais_alta:
            mais_alta = i['altura']
            nome_mais_alto = i['nome']

    print(f"A pessoa mais baixa é o {nome_mais_baixo} com {mais_baixa} cm."
          f"\nA pessoa mais alta é o {nome_mais_alto} com {mais_alta} cm.")

exercicios_json()
print('=======//=======')
imc_de_todos()
print('=======//=======')
imc_homem()
print('=======//=======')
imc_mulher()
print('=======//=======')
media_imc_homem()
print('=======//=======')
media_imc_mulher()
print('=======//=======')
pessoa_alta_baixa()