num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco')
while True:
    pedido = int(input('Qual valor entre 0 e 5 deseja ver por extenso: '))
    if 5 >= pedido >= 0:
        print(f'Você digitou o número {num[pedido]}')
        break
    else:
        print('O valor deve ser entre 0 e 5')
        print('-' *20)