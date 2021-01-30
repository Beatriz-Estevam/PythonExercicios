Peso = float(input('Insira o Peso em Kg: '))
Altura = float(input('Insira a Altura (ex: 1.80): '))
IMC = (Peso / (Altura * Altura))
if (IMC) < 18.5:
    print('Abaixo do Peso ideal')
elif 18.5 <= (IMC) < 25:
    print('Peso ideal')
elif 25 <= (IMC) < 30:
    print('Sobrepeso')
elif 30 <= (IMC) < 40:
    print('Obesidade')
elif (IMC) > 40:
    print('Obesidade mórbida')
print('Você possui {:.2f} de IMC'.format(IMC))
