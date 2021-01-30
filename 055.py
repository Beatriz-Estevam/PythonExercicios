# Faça um programa que leia o peso de 5 pessoas . No final mostre qual foi o maior e o menos peso lidos
Maior = 0
Menor = 0
for c in range(1, 5+1):
    Peso = float(input('[{}] Qual o seu peso em Kg: '.format(c)))
    if c == 1:
        Maior = Peso
        Menor = Peso
    else:
        if Peso >= Maior:
            Maior = Peso
        elif Peso <= Menor:
            Menor = Peso
print('Maior = {}'.format(Maior))
print('Menor = {}'.format(Menor))
