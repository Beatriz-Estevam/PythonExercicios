linhas = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para {[l, c]}'))
        linhas[l].append(valor)
print('-=' * 10)
for l in range(0, 3):
    print()
    for c in range(0, 3):
        print(linhas[l][c], end=' ')
