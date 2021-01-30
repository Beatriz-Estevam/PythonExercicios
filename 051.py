# Desenvolva um programa que leia o primeiro termo e a razão de uma PA no final, mostre os 10 primeiros termos dessa progressão
print("=" * 36)
print('        10 TERMOS DE UMA PA        ')
print('=' * 36)
PrimeiroTermo = float(input('Qual o \033[35mPRIMEIRO TERMO\033[m da PA?: '))
Razão = float(input('Qual a \033[32mRAZÃO\033[m da PA: '))
print('\033[35mPRIMEIRO TERMO\033[m {}'.format(PrimeiroTermo))
print('\033[32mRAZÃO\033[m {}'.format(Razão))
print('=' * 36)
for c in range(1, 10+1):
    print('{:.0f} ->'.format(PrimeiroTermo + (c - 1) * Razão), end=' ')
print('FIM')

