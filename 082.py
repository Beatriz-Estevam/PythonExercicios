all = []
par = []
impar = []
while True:
    all.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for n in all:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(30 * '-=')
print(f'A lista total é {all}')
print(f'A lista par é {par}')
print(f'A lista impar é {impar}')

