import random

# Números mais sorteados na história da Mega da Virada
numeros_frequentes = [5, 10, 20, 33, 36, 58]


def gerar_aposta(qtd=6):
    """
    Gera uma aposta para a Mega da Virada.
    Por padrão, usa os números mais frequentes.
    Se qtd > len(numeros_frequentes), completa com números aleatórios.
    """
    aposta = numeros_frequentes.copy()

    # Se precisar de mais números, completa aleatoriamente
    if qtd > len(aposta):
        restantes = [n for n in range(1, 61) if n not in aposta]
        aposta += random.sample(restantes, qtd - len(aposta))

    # Embaralha para não ficar sempre na mesma ordem
    random.shuffle(aposta)
    return aposta[:qtd]


# Exemplo de uso
print("Sua aposta sugerida:", gerar_aposta())

