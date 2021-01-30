NotaProva1 = float(input('Insira a nota da \033[31mPROVA 1\033[m: '))
NotaProva2 = float(input('Insira a nota da \033[31mPROVA 2\033[m: '))
if (NotaProva1 + NotaProva2) / 2 < 5:
    print('Média igual a \033[31m{:.2f}\033[m menor de \033[31m5.0\033[m'.format((NotaProva1 + NotaProva2) / 2))
    print('Situação: \033[31mREPROVADO\033[m')
elif 6.9 > (NotaProva1 + NotaProva2) / 2 > 5:
    print('Média igual a \033[33m{:.2f}\033[m entre de \033[33m5.0 e 6.9\033[m'.format((NotaProva1 + NotaProva2) / 2))
    print('Situação: \033[33mRECUPERAÇÃO\033[m')
elif (NotaProva1 + NotaProva2) / 2 >= 7:
    print('Média igual a \033[32m{:.2f}\033[m maior ou igual a \033[32m7.0\033[m'.format((NotaProva1 + NotaProva2) / 2))
    print('Situação: \033[32mAPROVADO\033[m')
