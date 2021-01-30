from random import randint
num = randint(0, 5)
chute = int(input('Pensei em um número! Chute qual foi esse número! Dica: foi entre 0 e 5: '))
if chute == num:
    print('PARABÉNS!! VOCÊ ACERTOU')
    print('O número é {} e você chutou {}'.format(num, chute))
else:
    print('OPS! VOCÊ ERROU!')
    print("Tente novamente")
    print('O número era {} e você chutou {}'.format(num, chute))


