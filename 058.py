#ERRADO
from random import randint
from time import sleep
cont = 0

print('=x' * 25)
print ('             \033[35mJOGO DA ADIVINHAÇÃO\033[m           ')
print('=x' * 25)

print('\033[36mComputador:\033[m Eu pensei em um número, \033[31mtente\033[m adivinhar')
print('\033[35mDICA: Foi entre 0 e 10!\033[m')
num = int(randint(0, 10))
chute = int(input('\033[32mJogador: \033[mEu pensei no número '))

print('\n\033[31mO RESULTADO FOI\033[m')

for timmer in range(1, 4):
    sleep(1)
    print('.', end='')

while chute != num:
    print('\n\033[31mOPS! VOCÊ ERROU!\033[m')
    print('\033[36mComputador:\033[m Ahá, eu ganhei. O número era \033[31m{}\033[m e você chutou {}'.format(num, chute))
    sleep(1)
    print("\n\033[35mTente novamente\033[m")
    cont += 1
    chute = int(input('\033[32mJogador: \033[mEu pensei no número '))
    print('\n\033[31mO RESULTADO FOI\033[m')
    for timmer in range(1, 4):
        sleep(1)
        print('.', end='')

print('\n\033[32mPARABÉNS! VOCÊ ACERTOU!\033[m')
print('\033[36mComputador:\033[m AAA, que droga!. O número era \033[31m{}\033[m e você chutou {}'.format(num, chute))
print("\033[35mVOCÊ PRECISOU DE {} TENTATIVA(S) PARA GANHAR DO COMPUTADOR\033[m".format(cont))
print('=x' * 25)
