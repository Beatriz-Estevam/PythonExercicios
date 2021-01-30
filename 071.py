print('=' * 30)
print('{:^30}'.format('BANCO DO BRASIL'))
print('=' * 30)
valor = cont50 = cont20 = cont10 = cont1 =0
while True:
    valor = int(input('Qual valor você quer sacar? R$'))
    while valor - 50 >= 0:
        valor -= 50
        cont50 += 1
    while valor - 20 >= 0:
        valor -= 20
        cont20 += 1
    while valor - 10 >= 0:
        valor -= 10
        cont10 += 1
    while valor - 1 >= 0:
        valor -= 1
        cont1 += 1
    if valor == 0:
        break
print(f'Total de {cont50} cédulas de R$50' if cont50 != 0 else '')
print(f'Total de {cont20} cédulas de R$20' if cont20 != 0 else '')
print(f'Total de {cont10} cédulas de R$10' if cont10 != 0 else '')
print(f'Total de {cont1} cédulas de R$1' if cont1 != 0 else '')
print('=' * 30)
print('Volte sempre ao BANDO DO BRASIL! Tenha um bom dia!')
