from datetime import date
Ano = int(input('Qual ano você quer saber se é bissexto? (Coloque 0 para a data atual): '))
if Ano == '0':
    Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print('{} é ano Bissexto'.format(Ano))
else:
    print('{} não é Bissexto'.format(Ano))