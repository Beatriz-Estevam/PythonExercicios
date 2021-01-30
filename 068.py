from random import randint
contador = 0
Status = ''
valor_humano = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)

while True: #soma % 2 and Par_Impar = 'P'
    valor_humano = int(input('Diga um valor: '))
    Par_Impar = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    while Par_Impar not in 'IP':
        print('VALOR NÃO VÁLIDO, DIGITE [P] PARA PAR E [I] PARA ÍMPAR')
        Par_Impar = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    if Par_Impar == 'I':
        Par_Impar = 'ÍMPAR'
    else:
        Par_Impar = 'PAR'
    valor_cpu = randint(0, 10)
    soma = valor_cpu + valor_humano
    if (soma % 2) == 0:
        Status = 'PAR'
    else:
        Status = 'ÍMPAR'
    print(f'Você jogou {valor_humano} e o computador {valor_cpu}. Total de {soma} DEU {Status}')
    if Status != Par_Impar:
        break
    contador += 1
    print('-' * 20)
    print('VOCÊ VENCEU!')
    print('Vamos jogar novamente...')
    print('-=' * 20)
print('VOCÊ PERDEU!')
print('-=' * 20)
print(f'GAME OVER! Vocẽ venceu {contador} vez(es)')


