from math import sqrt, pow

CAdj = float(input('Valor do Cateto Adjacente: '))
COpo= float(input('Valor do Cateto Oposto: '))
Hipo = sqrt(pow(CAdj, 2)+pow(COpo, 2))
print('Com o Cateto Adjacente igual a {} e o Cateto oposto igual a {}, a hipotenusa é {}'.format(CAdj, COpo, Hipo))
