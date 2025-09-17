'''

Radar com tolerância de chuva
Leia vel, limite, chovendo (S/N). A tolerância é +10% do limite apenas se chover. Multa se vel > limite quando não
chove ou vel > limite * 1.10 quando chove.

'''

velocidade = float(input("Velocidade registrada (km/h): "))

limite = float(input("Limite de velocidade (km/h): "))

chovendo = input("Está chovendo? (S/N): ").strip().upper()

if chovendo == 'S':
    tolerancia = limite * 1.10

    if velocidade > tolerancia:
        print("Multa aplicada (com tolerância de chuva).")

    else:
        print("Sem multa (com tolerância de chuva).")

elif chovendo == 'N':

    if velocidade > limite:
        print("Multa aplicada (sem tolerância).")

    else:
        print("Sem multa (sem tolerância).")

else:
    print("Entrada inválida para condição de chuva.")
