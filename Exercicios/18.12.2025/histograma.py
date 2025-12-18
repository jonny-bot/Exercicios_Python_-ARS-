from collections import Counter

dados = [2, 3, 4, 2, 5, 3, 2, 4, 5, 5, 5]

# Contagem de frequência
freq = Counter(dados)

print(freq)
# Saída: Counter({5: 4, 2: 3, 3: 2, 4: 2})
