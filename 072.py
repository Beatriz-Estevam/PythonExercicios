while True:
    NumPedido = int(input('Digite um número entre 0 e 20: '))
    if 0 <= NumPedido <= 20:
        break
    print('Opção inválida. ', end='')
NumExtenso =('zero', 'um',  'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezessies', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número {NumExtenso[NumPedido]}')
