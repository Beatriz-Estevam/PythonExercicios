valor = 0
s = 0
count = 0
valor = int(input('Digite um valor [999 para parar]: '))
while valor != 999:
    s += valor
    count +=1
    valor = int(input('Digite um valor [999 para parar]: '))
print('Vocẽ digitou {} com o flag, {} sem o flag, somando {} sem o flag e {} com o flag'.format(count, count-1, s - 999, s ))
print('Vocẽ digitou {} numeros sem o flag, somando {}'.format( count, s))
