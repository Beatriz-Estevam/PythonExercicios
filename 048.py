#  Faça um programa que calcule a soma entre números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500
s = 0
for c in range (1, 500+1, 2):
    if c % 3 == 0:
        s += c
print('A soma é {}'.format(s))
print('FIM')
