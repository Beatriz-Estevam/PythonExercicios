# Faça um contagem regressiva para o estouro de fogos de artifício indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep
print('\033[35mCONTAGEM REGRESSIVA PARA O ANO NOVO\033[034m')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(0)
print('\033[32mFELIZ ANO NOVOOO')
