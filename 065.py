resposta = 'S'
maior = menor = s = count = 0
while resposta == 'S':
    count += 1
    valor = int(input('Digite um valor : '))
    s += valor
    if count == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
    resposta = str(input('Deseja continuar [S/N]: ')).upper()
    if resposta != 'S' and resposta != 'N':
        print('VALOR NÃO COMPUTÁVEL ')
        print('Dgite [S] para continuar e [N] para parar')
        resposta = str(input('Deseja continuar [S/N]: ')).upper()
print(20 * '-=')
print('A média dos valores que você digitou vale: {}'.format(s/count))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
