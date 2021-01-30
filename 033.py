n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
if n1 > n2 > n3:
    print('O maior valor é {}'.format(n1))
    print('O menor valor é {}'.format(n3))
if n1 > n3 > n2:
    print('O maior valor é {}'.format(n1))
    print('O menor valor é {}'.format(n2))
if n2 > n1 > n3:
    print('O maior valor é {}'.format(n2))
    print('O menor valor é {}'.format(n3))
if n2 > n3 > n1:
    print('O maior valor é {}'.format(n2))
    print('O menor valor é {}'.format(n1))
if n3 > n1 > n2:
    print('O maior valor é {}'.format(n3))
    print('O menor valor é {}'.format(n2))
if n3 > n2 > n1:
    print('O maior valor é {}'.format(n3))
    print('O menor valor é {}'.format(n1))
if n1 == n2 > n3 :
    print('O maior valor é : {}'.format(n2))
    print('O maior valor é : {}'.format(n3))
if n1 == n3 > n2 :
    print('O maior valor é : {}'.format(n1))
    print('O maior valor é : {}'.format(n2))
if n3 == n2 > n1 :
    print('O maior valor é : {}'.format(n2))
    print('O maior valor é : {}'.format(n1))
if n1 > n3 == n2 :
    print('O maior valor é : {}'.format(n1))
    print('O maior valor é : {}'.format(n3))
if n2 > n3 == n1 :
    print('O maior valor é : {}'.format(n2))
    print('O maior valor é : {}'.format(n3))
if n3 > n1 == n2 :
    print('O maior valor é : {}'.format(n3))
    print('O maior valor é : {}'.format(n1))
if n1 == n3 == n2 :
    print('Não existe valor maior ou menor, são todos iguais')
