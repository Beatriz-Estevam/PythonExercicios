num = int(input('Fatorial de '))
multi = num
fac = num
while multi != 1: # QUANDO O fator CHEGAR A 0, PARA A CONTA
    multi = multi - 1 #Diminui 1 de Num para ser levado para a aultiplicação do fatorial
    fatores = (num - multi)
    fac = fac * fatores
print('O fatorial de {} é igual a {}'.format(num, fac))
print('FIM')
