info = ('Arroz', 2.50, 'Feijão', 3)
count = 0

print(40 * '-')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(40 * '-')
for infos in info:
    if count % 2 == 0:
        print(f'{info[count]:.<31}', end='')
    elif count % 2 != 0:
        print(f'R$ {info[count]:>7.2f}')
    count += 1
print(40 * '-')
