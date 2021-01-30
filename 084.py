pessoa = []
pessoal = []
pesado = leve = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if len(pessoal) == 0:
        pesado = leve = pessoa[1]
    else:
        if pessoa[1] > pesado:
            pesado = pessoa[1]
        if pessoa[1] < leve:
            leve = pessoa[1]
    pessoal.append(pessoa[:])
    pessoa.clear()
    r = str(input('Quer continuar? [S/N] ')).strip()
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você cadastrou {len(pessoal)} pessoas')
print(f'O maior peso é de {pesado}kg. Peso de ', end='')
for nome in pessoal:
    if nome[1] == pesado:
        print(nome[0], end='')
print(f'\nO menor peso é de {leve}kg. Peso de ', end='')
for nome in pessoal:
    if nome[1] == leve:
        print(nome[0], end='')
