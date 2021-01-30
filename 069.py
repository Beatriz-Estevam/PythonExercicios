maioresdeidade = homens = mulheres = 0
while True:
    print(20 * '-')
    print('CADASTRE UMA PESSOA')
    print(20 * '-')
    idade = int(input('Quantos anos você tem: '))
    sexo = str(input('Qual o seu sexo? [F/M] ')).upper().strip()[0]
    print(20 * '-')

    if idade > 18:
        maioresdeidade += 1

    while sexo not in 'MF':
        print('Valor não computado. Digite [F] para sexo feminino e [M] para sexo masculino')
        sexo = str(input('Qual o seu sexo? [F/M] ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    resp = str(input('Deseja continuar:? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        print('Valor não computado. Digite [S] para continuar e [N] para parar')
        resp = str(input('Deseja continuar:? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print(20 * '=')
print('FIM DO PROGRAMA')
print(20 * '=')
print(f'Temos {mulheres} mulheres com menos de 20 anos\nAo todo temos {homens} homens cadastrados \nTotal de pessoas com mais de 18 anos: {maioresdeidade}')
