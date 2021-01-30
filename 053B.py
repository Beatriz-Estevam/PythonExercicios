frase = input('Digite uma frase: ').upper().strip()
TudoJunto = frase.replace(' ', '')
Inverso = ''
print('Você digitou: {}'.format(frase))
for letra in range(len(TudoJunto) - 1, -1, -1):
    Inverso += TudoJunto[letra]
print('A frase que você digitou invertida fica: {}'.format(Inverso))
if frase == Inverso:
    print('É um palindromo')
else:
    print('Não é um palíndromo')
