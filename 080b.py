valores = []
for c in range(1, 6):
    novovalor = int(input('Digite um valor: '))
    if not valores:
        valores.append(novovalor)
        print('Primeiro valor adicionado a lista...')
    elif novovalor > valores[(len(valores)-1)]:
        valores.append(novovalor)
        print('Adicionado no final da lista...')
    else:
        contador = 0
        while novovalor > valores[contador]:
            contador += 1
        valores.insert(contador, novovalor)
        for p, n in enumerate(valores):
            if n == novovalor and len(valores) == c:
                print(f'Adicionado na posição {p}')
print('=-' * 30)
print(valores)
