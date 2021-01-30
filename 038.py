print('\033[35mVERIFICADOR DE NÚMEROS\033[m')
Num1 = int(input('Digite o \033[31mPrimeiro\033[m valor: '))
Num2 =int(input('Digite o \033[34mSegundo\033[m valor: '))
if Num1 > Num2:
    print('O \033[31mPrimeiro Valor \033[mé \033[35mMAIOR\033[m que o \033[34mSegundo valor\033[m')
elif Num1 < Num2:
    print('O \033[31mPrimeiro Valor \033[mé \033[35mMENOR\033[m que o \033[34mSegundo valor\033[m')
elif Num1 == Num2:
    print('Não existe \033[35mMAIOR VALOR\033[m nem \033[35mMENOR VALOR\033[m, por que o \033[31mPrimeiro Valor\033[m e o \033[34 Segundo Valor\033[m são \033[36m IGUAIS\033[m')
