x = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    x += 1
    soma += n
print(f'A soma dos {x} valores foi {soma}!')
