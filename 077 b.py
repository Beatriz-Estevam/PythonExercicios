ListaDePalavras = ('Beatriz', 'Pudim', 'Carregador', 'Meia')
for palavras in ListaDePalavras:
    print(f'\n As vogais de {palavras} são: ', end='')
    for letras in palavras:
        if letras.upper().strip() in 'AEIOU':
            print(f'{letras}', end=' ')
