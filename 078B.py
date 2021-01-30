valores = []
mai = men = 0
#pos = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    #pos += 1
    if cont == 0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]
print(30 * '=-')
print(f'Vocẽ digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for c, valor in enumerate(valores):
    if valor == mai:
        print(f'{c}... ', end='')
print(f'\nO menor valor digitado foi {men} nas posições ', end='')
for c, valor in enumerate(valores):
    if valor == men:
        print(f'{c}... ', end='')
