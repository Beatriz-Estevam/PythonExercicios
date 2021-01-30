frase = []
frase.append(input('Digite uma expressão ').split())
aberto = fechado = aberto1 = fechado1 = 0
'''
if '(' in frase:
    aberto = (frase.count('('))
if ')' in frase:
    fechado = (frase.count('('))
if aberto != fechado:
    print('Expressão inválida')
'''
while frase.find('(') > frase.find(')'):
    aberto1 = frase.find('(')
    fechado1 = frase.find(')')
    frase.pop(aberto1)
