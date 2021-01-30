sexo = str(input(('Informe seu sexo [M/F]:' ))).strip().upper()[0] #PEGA SO A 1 LETRA - FATIAMENTO
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucsso'.format(sexo))
