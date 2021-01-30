linhas = [[], [], []]
s = s3c = maior2l = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para {[l, c]}'))
        linhas[l].append(valor)
        if valor % 2 == 0:
            s += valor
        if c == 2:
            s3c += valor
        if l == 1:
            if c == 0:
                maior2l = valor
            elif valor > maior2l:
                maior2l = valor
print('-=' * 10)
for l in range(0, 3):
    for c in range(0, 3):
        print(linhas[l][c], end=' ')
    print()
print(f'A soma de todos os valores pares é {s}')
print(f'A soma dos valores da terceira coluna é {s3c}')
print(f'O maior valor da segunda linha é {maior2l}')