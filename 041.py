from datetime import date
AnodeNascimento = int(input('Insira o ano de nascimento do Atleta: '))
if (date.today().year - AnodeNascimento) <= 9:
    print('MIRIM')
elif 9 < (date.today().year - AnodeNascimento) <= 14:
    print('INFANTIL')
elif 14 < (date.today().year - AnodeNascimento) <= 19:
    print('JUNIOR')
elif 19 < (date.today().year - AnodeNascimento) <= 20:
    print('SÊNIOR')
elif (date.today().year - AnodeNascimento) >= 20:
    print('MESTER')
print('Você tem {} anos'.format((date.today().year - AnodeNascimento)))
