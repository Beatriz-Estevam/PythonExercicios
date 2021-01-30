# Crie um programa que leia o ano de nascimento de sete pessoas, no final mostre qantas pessoas ainda nao atingiram a maioridade e quantas já são maiores (21 anos)
from datetime import date
maiores = 0
menores = 0
for c in range(1, 7+1):
    Ano = int(input('{} - Que ano vocẽ nasceu: '.format(c)))
    idade = date.today().year - Ano
    if idade >= 21:
        maiores += 1
    elif idade < 21:
        menores += 1
print('Maiores = {}'.format(maiores))
print('Menores = {}'.format(menores))
