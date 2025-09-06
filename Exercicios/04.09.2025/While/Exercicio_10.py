import random

opcoes = ['pedra', 'papel', 'tesoura']

escolha_jogador = input('Escolha: Pedra, Papel ou Tesoura: ').lower()

escolha_maquina = random.choice(opcoes)

print(f'A escolha da Máquina foi: {escolha_maquina} e a sua foi: {escolha_jogador}')

if escolha_jogador == escolha_maquina:
    print('Deu EMPATE!!!')

elif (escolha_jogador == 'pedra' and escolha_maquina == 'tesoura') or (escolha_jogador == 'papel' and escolha_maquina == 'pedra') or (escolha_jogador == 'tesoura' and escolha_maquina == 'papel'):
    print('Você venceu!!!')
else:
    print('A Máquina Venceu!!!')