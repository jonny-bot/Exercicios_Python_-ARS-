try:
    idade = int(input('Digite a idade: '))

    cnh = input("Tem CNH? (S/N): ").strip().upper()

    if idade >= 18 and cnh == 'S':
        print("Pode dirigir")
        
    else:
        print("Não pode")

except ValueError:
    print("Digite uma entrada válida!")
