# Faça um programa que mostre na tela todos os números pares que estão entre 1 e 50
for c in range(1, 51, 2):
    print('\033[36m{},'.format(c+1), end=' ')
print('FIM')
