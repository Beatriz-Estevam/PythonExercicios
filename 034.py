Sal = float(input('Digite o seu salário para saber o aumento: R$'))
if Sal > 1250.00:
    print('Seu aumento é de R${:.2f} e seu salário ficará sendo de R$ {:.2f}'.format(Sal*0.1, Sal*0.1+Sal))
if Sal <= 1250.00:
    print('Seu aumento é de R${:.2f} e seu salário ficará sendo de R$ {:.2f}'.format(Sal*0.15, Sal*0.15+Sal))
