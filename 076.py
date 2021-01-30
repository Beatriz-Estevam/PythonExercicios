informações = ('Leite', 2.95, 'Pão', 5.60, 'Alface', 2.30, 'Molho de tomate', 0.95, 'Macarrão', 5.30, 'Quijo ralado', 7.98, 'Vinho Chileno', 250.00,)
print('-' * 43)
print(f'{"LISTAGEM DE PREÇO":^43}')
print('-' * 43)
for pos in range(0, len(informações)):
    if pos % 2 == 0:
        print(f'{informações[pos]:.<32}', end='')
    else:
        print(f' R$ {informações[pos]:>6}')
print('-' * 43)
