import json
import random

contador_peso = 0
lista_perguntas = []

with open('Arquivos(Json)/exercicio1.json', 'r', encoding='utf-8') as xyz:
    perguntas = json.load(xyz)

    pergunta = random.sample(perguntas, 28)

    for indice, item in enumerate(pergunta):
        pergunta = item.get("Pergunta")
        peso = item.get("Peso")

        print(f'{indice + 1}° Pergunta: {pergunta} || Peso: {peso}')

        while True:
            try:
                resposta = int(input("1 - SIM || 2 - NÃO\n"
                                     "Digite a Resposta Correta: "))

                if resposta == 1:
                    print("Você escolheu SIM")
                    contador_peso += peso
                    break

                elif resposta == 2:
                    print("Você escolheu NÃO")
                    break

                else:
                    print(f"Você digitou {resposta}, que não é 1 nem 2. Tente novamente.")

            except ValueError:
                print("Digite uma entrada válida (apenas números).")

        temp = 'Pergunta: ' + pergunta + ' || Peso: ' + str(peso) + ' || Resposta: ' + str(resposta)
        lista_perguntas.append(temp)

contador = 0
for i in lista_perguntas:
    contador += 1
    print(f'{contador}° {i}')

lista = {
    1: 'Pessoa Inocente!',
    2: 'Pessoa Suspeita!',
    3: 'Pessoa Cúmplice!',
    4: 'Assassina!'
}

if 0 <= contador_peso <= 15:
    print(f'Conclusão: {lista[1]}')

elif 16 <= contador_peso <= 30:
    print(f'Conclusão: {lista[2]}')

elif 31 <= contador_peso <= 45:
    print(f'Conclusão: {lista[3]}')

elif 46 <= contador_peso <= 67:
    print(f'Conclusão: {lista[4]}')

print(f'Contador de Sim: {contador_peso}')
