total = Mais1000 = cont = MaisBarato = 0
NomeMaisBrato = ''

print(30 * '-')
print('{:^30}'.format(' LOJA SUPER BARATÃO '))
print(30 * '-')

while True:
    cont += 1
    produto = str(input('Nome do produto: ')).strip()
    Preço = float(input('Preço: R$'))
    total += Preço

    if Preço > 1000:
        Mais1000 += 1

    if cont == 1 or Preço < MaisBarato:
        MaisBarato = Preço
        NomeMaisBrato = produto

    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continua not in 'NS':
        print('O valor não pode ser computado. Digite [S] para continuar e [N] para parar')
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break

print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O valor total das compras foi de {total}')
print(f'Temos {Mais1000} produtos que custam mais de R$ 1000.00')
print(f'O produto mais barato foi {NomeMaisBrato} custando R${MaisBarato:.2f}')
