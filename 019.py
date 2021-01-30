import random

nome1 = input('Nome do Aluno 1: ')
nome2 = input('Nome do Aluno 2: ')
nome3 = input('Nome do Aluno 3: ')
nome4 = input('Nome do Aluno 4; ')
seq = [nome1, nome2, nome3, nome4]
sorteado = random.choice(seq)
print('O Aluno sorteado para apagar o quadro é: {}'.format(sorteado))
