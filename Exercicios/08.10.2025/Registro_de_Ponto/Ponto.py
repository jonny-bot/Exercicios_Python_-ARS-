import json
from datetime import datetime

with open('funcionarios.json', 'r', encoding='utf-8') as f:
    funcionarios = json.load(f)

def obter_nome_por_id():
    id_funcionario = input('Digite o seu ID de Funcionário: ')
    nome = funcionarios.get(id_funcionario)
    if nome:
        return nome
    else:
        print("ID não encontrado. Tente novamente.")
        return obter_nome_por_id()

def horario():
    agora = datetime.now()
    hora = agora.hour
    minuto = agora.minute

    if hora < 12:
        print('Você Bateu o Ponto da Entrada do Trabalho!!!')
        return 'Entrada do Trabalho'
    elif hora == 12:
        print('Você Bateu o Ponto da Entrada do Almoço!!!')
        return 'Entrada do Almoço'
    elif hora == 13:
        print('Você Bateu o Ponto da Volta do Almoço!!!')
        return 'Volta do Almoço'
    elif hora >= 17 and minuto >= 48:
        print('Você Bateu o Ponto do Final do Expediente!!!')
        return 'Final do Expediente'
    else:
        print('Horário não identificado para ponto.')
        return 'Outro Horário'

def registrar_ponto(nome):
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
    tipo_ponto = horario()

    print(f'''
=======X {tipo_ponto} X=======
COMPROVANTE DE REGISTRO DE PONTO
        DO TRABALHADOR
ARS IND. COM. DE PARAF. FERRAGENS LTDA
CNPJ: 123456789
CEI: 000000000000
AV. QUEIROS DOS SANTOS, 690/700/710
{nome}
PIS: 000000000000
NSR: 00000000
Data/Hora: {data_formatada}
''')

    return {
        "Nome do Funcionário": nome,
        "Tipo de Ponto": tipo_ponto,
        "Data/Hora": data_formatada
    }

nome = obter_nome_por_id()
novo_registro = registrar_ponto(nome)

try:
    with open('registro_de_ponto.json', 'r', encoding='utf-8') as f:
        registros = json.load(f)
except FileNotFoundError:
    registros = []

registros.append(novo_registro)

with open('registro_de_ponto.json', 'w', encoding='utf-8') as f:
    json.dump(registros, f, ensure_ascii=False, indent=4)
