Velocid = float(input('Qual a veloidade do carro em Km/h: '))
if Velocid > 80.0:
    print('VOCÊ FOI MULTADO')
    print('Você deve pagar R$ {:.2f} de multa'.format((Velocid - 80) * 7))
