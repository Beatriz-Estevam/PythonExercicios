from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar 
    [2] Mutiplicar
    [3] Maior 
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('>>>>>Qual a sua opção: '))
    print('-=' * 20)
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            maior = 'nenhum, eles são iguais'
        print('O maior valor entre {} e {} é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizado...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente')
print('Fim do Programa! VOLTE SEMPRE!')
