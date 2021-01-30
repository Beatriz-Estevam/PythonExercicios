# Refaça o desafio 009 mostrado a tabulada de um número que o usuário escolher, só que agora utilizando o laço for.
tab = int(input('Você quer ver a tabada do número: '))
print('-*' * 6)
print('TABUADA DO {}'.format(tab))
print('-*'*6)
for c in range(1, 10+1):
    print('{} x {:2} = {}'.format(tab, (c), (tab * (c))))
print('-*'*6)
