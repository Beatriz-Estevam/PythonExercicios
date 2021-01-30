c = float(input('Qual o valor da reta 1: '))
b = float(input('Qual o valor da reta 2: '))
a = float(input('Qual o valor da reta 3: '))
if (b - c) < a < (b + c):
    if (a - c ) < b < (a + c):
        if ( a - b ) < c < (a + b):
            print('As retas {}, {}, {} PODEM formar um triângulo'.format(a, b, c))
        else:
            print(('As retas {}, {}, {} NÃO PODEM formar um triângulo'.format(a, b, c)))
    else:
        print(('As retas {}, {}, {} NÃO PODEM formar um triângulo'.format(a, b, c)))
else:
    print(('As retas {}, {}, {} NÃO PODEM formar um triângulo'.format(a, b, c)))
