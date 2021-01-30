c = float(input('Qual o valor da reta 1: '))
b = float(input('Qual o valor da reta 2: '))
a = float(input('Qual o valor da reta 3: '))
if (b - c) < a < (b + c) and (a - c ) < b < (a + c) and ( a - b ) < c < (a + b):
    print('As retas {}, {}, {} PODEM formar um triângulo'.format(a, b, c))
    if a == b == c:
        print('Formam um triângulo equilátero')
    elif a == b != c or a == c != b or b == c != a:
        print('Formam um triângulo isósceles')
    elif a != b != c != a:
        print('Formam um triângulo escaleno')
else:
    print(('As retas {}, {}, {} NÃO PODEM formar um triângulo'.format(a, b, c)))
