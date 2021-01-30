exp = str(input('Digite uma expressão: '))
pilha = []
inv = 'False'
for parte in exp:
    if parte == '(':
        pilha.append('(')
    elif parte == ')':
        if len(pilha) == 0:
            pilha.append('(')
            break
        if len(pilha) > 0:
            pilha.pop()
if len(pilha) > 0:
    print('INVÁLIDO')
elif len(pilha) == 0:
    print('SUCESSO')



