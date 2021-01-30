from random import randint
ordem = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for números in ordem:
    print(f'{números}', end=' ')
print(f'\nO valor máximo é {max(ordem)}')
print(f'O valor minimo é {min(ordem)}')
