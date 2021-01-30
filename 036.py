ValordaCasa = float(input('Qual o valor da casa: R$ '))
Salario = float(input('Qual o salário do comprador: R$ '))
Anos = int(input('Em quantos anos vai pagar a casa: '))
if ValordaCasa/(12 * Anos) > (30 / 100) * Salario:
    print('EMPRÉSTIMO NEGADO')
    print('O valor máximo da prestação mensal com base no salário de R$ {:.2f} é de R$ {:.2f}'.format(Salario, Salario * (30 / 100)))
    print('O valor do empréstimo mensal seria de {:.2f}'.format(ValordaCasa / (12 * Anos)))
else:
    print('EMPRÉSTIMO APROVADO')
    print('O valor máximo da prestação mensal com base no salário de R$ {:.2f} é de R$ {:.2f}'.format(Salario, Salario * (30 / 100)))
    print('O valor do empréstimo mensal é de {:.2f}'.format(ValordaCasa / (12 * Anos)))
print('TENHA UM BOM DIA')
