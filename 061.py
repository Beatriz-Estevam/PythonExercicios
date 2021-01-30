primeiro = int(input(('Primeiro termo: ')))
razão = int(input('Razão: '))
sub = 0
x = 0
while x != 10:
    x += 1
    n = primeiro + (x - 1) * razão
    print('{}'.format(n), end=' -> ')
print('FIM')

#ATÉ AQUI DESAFIO 061, DAQUI PRA FRENTE 062

continuar = 'S'
while continuar == 'S':
    continuar = str(input(('\nDeseja mostrar mais termos [S/N]? '))).upper()
    while continuar != 'S' and continuar != 'N':
        print('Opção inválida. TENTE NOVAENTE')
        continuar = str(input(('\nDeseja mostrar mais termos [S/N]? '))).upper()

    if continuar == 'S':
        termos = int(input('Quantos termos da pa você deseja ver? '))
        sub = 0
        x = 0
        while x != termos:
            x += 1
            n = primeiro + (x - 1) * razão
            print('{} -> '.format(n), end='')
    else:
        print('Até logo, volte sempre!')
print('FIM')