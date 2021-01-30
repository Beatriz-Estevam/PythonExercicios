from datetime import date
AnodeNascimento = int(input('Ano de Nascimento: '))
if date.today().year - AnodeNascimento == 18:
    print('HORA DO ALISTAMENTO')
    print('Você deve se alistar em {}'.format(AnodeNascimento + 18))
elif date.today().year - AnodeNascimento > 18:
    print('JÁ PASSOU {} ANO da hora dO ALISAMENTO'.format((date.today().year - AnodeNascimento)-18))
    print('Você deveria ter se alistado em {}'.format(AnodeNascimento + 18))
elif date.today().year - AnodeNascimento < 18:
    print('AINDA \033[31mNÃO\033[m PASSOU A DATA DO ALISTAMENTO, ainda faltam {} ano(s)'.format(18-(date.today().year - AnodeNascimento)))
    print('Seu alistamento deverá ver feito em {}'.format(AnodeNascimento + 18))
