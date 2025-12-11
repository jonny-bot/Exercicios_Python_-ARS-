import json
import random

soma_peso = 0
lista_resposta = []

with open('Arquivos(Json)/exercicio1.json', 'r', encoding='utf-8') as xyz:
    perguntas = json.load(xyz)

    pergunta = random.sample(perguntas, 28)

    print(f'São {len(pergunta)} Perguntas.')

    for indice,i in enumerate(pergunta):

        pergunta = i.get('Pergunta')
        peso = i.get('Peso')

        print(f'{indice + 1}° Pergunta: {pergunta} || Peso: {peso}')

        while True:
            try:

                escolha = int(input('1 - SIM || 2 - NÃO\n'
                                    'Digite: '))

                if escolha in (1,2):

                    if escolha == 1:
                        soma_peso += peso
                        resposta = 'SIM'
                        temp = f"Pergunta: {pergunta} || Peso: '{peso} || Resposta: {resposta}"
                        lista_resposta.append(temp)

                    if escolha == 2:
                        resposta = 'NÃO'
                        temp = f"Pergunta: {pergunta} || Peso: '{peso} || Resposta: {resposta}"
                        lista_resposta.append(temp)

                    break

                else:
                    print(f'Você Digitou {escolha}. Digite 1 ou 2.')

            except ValueError:
                print('Digite uma Entrada Válida!')

while True:
    try:

        opcao = int(input('0 - Sair do Programa\n'
                          '1 - Mostrar as Respostas\n'
                          '2 - Mostrar Total dos Pesos\n'
                          '3 - Mostrar Sentença\n'
                          'Digite umas das Opções: '))

        if opcao == 0:
            print('Saindo do Programa...')
            break

        if opcao == 1:

            for i in lista_resposta:
                print(i)

        if opcao == 2:
            print(f'Total dos Pesos: {soma_peso}')

        if opcao == 3:

            lista = {
                1: 'Pessoa Inocente!',
                2: 'Pessoa Suspeita!',
                3: 'Pessoa Cúmplice!',
                4: 'Assassino!'
            }

            if 0 <= soma_peso <= 15:
                print(f'Conclusão: {lista[1]}')

            elif 16 <= soma_peso <= 30:
                print(f'Conclusão: {lista[2]}')

            elif 31 <= soma_peso <= 45:
                print(f'Conclusão: {lista[3]}')

            elif 46 <= soma_peso <= 63:
                print(f'Conclusão: {lista[4]}')

            print(f'Contador de Sim: {soma_peso}')

    except ValueError:
        print('Digite uma Entrada Válida!')
