#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input('Digite um número: '))
if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num % 11 != 0:
    print('É primo ')
elif num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
    print('É primo')
else:
    print('Não é primo ')
#for c in range():