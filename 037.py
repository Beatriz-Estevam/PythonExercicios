num = int(input('Qual numero deseja converter: '))
Conv = int(input('Para qual base de conversão deseja converter \n[1] Para binário \n[2] Para octal \n[3] Para hexadecimal \nDigite o código: '))
if Conv == 1:
    print(bin(num)[2:])
elif Conv == 2:
    print(oct(num)[2:])
elif Conv == 3:
    print(hex(num)[2:])
else:
    print('Opção inválida, tente novamente')
