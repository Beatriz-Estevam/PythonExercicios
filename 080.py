valores = []
count = 0
while True:
    num = int(input('Digite um número: '))
    if not valores:
        valores.append(num)
    else:
        if num > valores[0]:
            while num > valores[count]:
                count += 1
                if count == len(valores):
                    valores.append(num)
                    count = 0
                    break
                elif num < valores[count]:
                    valores.insert(count, num)
                    count = 0
                    break
        else:
            valores.insert(count, num)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(valores)
