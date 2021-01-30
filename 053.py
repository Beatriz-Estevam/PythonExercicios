# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
TudoJunto = ''.join(palavras)
Inverso = ''
print('Você digitou: {}'.format(frase))
for letra in range(len(TudoJunto) - 1, -1, -1):
    Inverso += TudoJunto[letra]
print('A frase que você digitou invertida fica: {}'.format(Inverso))
if frase == Inverso:
    print('É um palindromo')
else:
    print('Não é um palíndromo')
