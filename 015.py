Kmantes = float(input('Km percorridos antes do aluguel: '))
Kmdepois = float(input('Km foram perorridos no final do aluguel: '))
diaalug = int(input('Dias alugados: '))
Valor_Dias = 60 * diaalug
Valor_Km = (Kmdepois - Kmantes) * 0.15
print('\nO valor a ser pago pelos dias alugados é de R${:.2f}'.format(Valor_Dias), end=' ')
print('e pelos Quilometros percorridos R${:.2f} \n'.format(Valor_Km))
print('O valor total a ser pago é de R${:.2f}'.format(Valor_Dias + Valor_Km))
