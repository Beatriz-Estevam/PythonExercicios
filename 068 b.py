from random import randint
v = 0
Status = ''
jogador = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)

while True: #soma % 2 and Par_Impar = 'P'
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = computador + jogador
    tipo = ' '
    while tipo not in 'IP':
        Par_Impar = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}', end=' ')
    if tipo == 'I':
        if soma % 2 == 0:
            print('VOCÊ PERDEU!')
            break
        else:
            print('VOCÊ VENDEU!')
            v += 1
    elif tipo == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Vocẽ venceu {v} vez(es)')
print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
