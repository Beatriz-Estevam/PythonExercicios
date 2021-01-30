valores = []
pos = 0
for cont in range(1, 6):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
    pos += 1
print(30 * '=-')
print(f'Vocẽ digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for c, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{c}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for c, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{c}... ', end='')

