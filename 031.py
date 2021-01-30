Km = float(input('Quantos Km terão sua viagem: '))
if Km > 200:
    print('Sua viagem custará: R${:.2f}'.format(Km*0.45))
if Km <= 200:
    print('Sua viagem custará: R$ {:.2f}'.format(Km*0.50))
