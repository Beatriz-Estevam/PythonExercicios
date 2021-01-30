from random import choices
Jogo = int(input('Digite: \n1)Pedra \n2)Papel \n3)Tesoura\nFAÇA SUA JOGADA: '))
opções = ['Pedra', 'Papel', 'Tesoura']
Pc = choices(opções)
Computador = Pc[0]
if Jogo == 1:
    Player = 'Pedra'
elif Jogo == 2:
    Player = 'Papel'
elif Jogo == 3:
    Player = 'Tesoura'

if Player == 'Pedra' and Computador == 'Pedra':
    print('Empate')
elif Player == 'Papel' and Computador == 'Papel':
    print('Empate')
elif Player == 'Tesoura' and Computador == 'Tesoura':
    print('Empate')
elif Player == 'Pedra' and Computador == 'Tesoura':
    print('VITÓRIA DO JOGADOR')
elif Player == 'Papel' and Computador == 'Pedra':
    print('VITÓRIA DO JOGADOR')
elif Player == 'Tesoura' and Computador == 'Papel':
    print('VITÓRIA DO JOGADOR')
elif Player == 'Pedra' and Computador == 'Papel':
    print('DERROTA')
    print('VITÓRIA DO COMPUTADOR')
elif Player == 'Papel' and Computador == 'Tesoura':
    print('DERROTA')
    print('VITÓRIA DO COMPUTADOR')
elif Player == 'Tesoura' and Computador == 'Pedra':
    print('DERROTA')
    print('VITÓRIA DO COMPUTADOR')
print('Computador: Eu joguei: {}'.format(Computador))
