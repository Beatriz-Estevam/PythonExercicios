#Quantidade = quantos elementos serão mostrados na sequência
quantidade = int(input('Quantos elementos da sequência de fibonacci você deseja ver? '))

início = '0 -> 1'
a1 = 0
a2 = 1
cont = 0
if quantidade == 1:
    print('0')
elif quantidade == 2:
    print('0 -> 1')
else:
    print('{} ->'.format(início), end='')
    while cont != (quantidade-2):
        cont += 1
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        print(' {} ->'.format(a3), end='')
print(' Fim')

