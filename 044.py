Preço = float(input('Insira o valor: R$ '))
CondiçãodePagamento = int(input('Condição de pagamento. Digite: \n1) A vista no dinheiro/cheque \n2) A vista no cartão \n3) 2x no cartão \n4)3x ou mais no cartão \n: '))
if CondiçãodePagamento == 1:
    print('Valor a ser pago a vista em dinheiro/cheque: R$ {}'.format(Preço - (0.10 * Preço)))
elif CondiçãodePagamento == 2:
    print('Valor a ser pago a vista no cartão: R$ {}'.format(Preço - (0.05 * Preço)))
elif CondiçãodePagamento == 3:
    print('Valor a ser pago 2x no cartão: R$ {}'.format(Preço))
elif CondiçãodePagamento == 4:
    parcela = int(input('Vai parcelar em quantas vezes?'))
    print('Valor a ser pago 3x ou mais no cartão: R$ {}'.format(Preço + (0.20 * Preço)))
    print('Serão {}x de {}'.format(parcela, ((Preço + (0.20 * Preço)) / parcela)))
