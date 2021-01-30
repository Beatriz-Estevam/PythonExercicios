from math import hypot

CAdj = float(input('Comprimento do Cateto Adjacente: '))
COpo= float(input('Comprimento do Cateto Oposto: '))
print('Com o Cateto Adjacente igual a {} e o Cateto oposto igual a {}, a hipotenusa é {}'.format(CAdj, COpo, hypot(CAdj, COpo)))
