num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
sequencia = (num1, num2, num3, num4)
print(sequencia)
print(f'O valor 9 apareceu {sequencia.count(9)} vez(es)')
if 3 in sequencia:
    print(f'O valor 3 apareceu na {(sequencia.index(3))+1}a posição')
else:
    print(f'O valor 3 não apareceu em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for numero in sequencia:
    if numero % 2 == 0:
        print(f'{numero} ', end='')