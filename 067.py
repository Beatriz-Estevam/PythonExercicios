while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(20 * '-')
    if n < 0:
        break
    for tab in range(0, 11):
        print(f'{n} x {tab:2} = {n * tab}')
    print(20 * '-')
print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')
