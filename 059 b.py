n1 = n2 = 0
opção = 4
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
while opção != 5:
    while opção != 4:
        if opção == 1:
            print('A soma vale: {}'.format(n1 + n2))
            opção = 4
        elif opção == 2:
            print('A multiplicação vale {}'.format(n1 * n2))
            opção = 4
        elif opção == 3:
            if n1 > n2:
                print('{} é maior que {}'.format(n1, n2))
                opção = 4
            elif n2 > n1:
                print('{} é maior que {}'.format(n2, n1))
                opção = 4
            else:
                print('{} é igual a {}'.format(n1, n2))
                opção = 4
    print('''Menu: 
    [1] Somar 
    [2] Multiplicar 
    [3] Maior 
    [4] Novos Números 
    [5] Sair''')
    opção = int(input('Opção: '))
print('Volte sempre"')

