# Desenvolva um programa que leia 6 nuumeros inteiros e mostre a soma apenas daqueles que forem pares. Se forem ímpares desconsidere-os
s = 0
Contador = 0
for c in range(1, 6+1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        Contador += 1
print('A soma de {} números pares dos {} que você me indicou é {}'.format(Contador, c, s))
