# Desenvolva um programa que leia o nome idade e sexo de 4 pessoas no final do programa mostre: 1)A média de idade do grupo, 2)nome do homem mais velho 3) Quatas mulheres tem menos de 20 ou 21 anos
IdadeMédia = 0
NomeHomemMaisVelho = ''
IdadeHomemMaisVelho = 0
MulheresMaiores = 0
MulheresMenores = 0
for c in range(1, 4+1):
    print('--- {} PESSOA ---'.format((c)))
    Nome = str(input('NOME: '))
    Idade = int(input('IDADE: '.format(c)))
    IdadeMédia += Idade
    Sexo = str(input('SEXO [F/M]: '.format(c)))
    if Sexo.upper() == 'M':
        if c == 1:
            IdadeHomemMaisVelho = Idade
            NomeHomemMaisVelho = Nome
            print('Idade', IdadeHomemMaisVelho)
            print('Nome', NomeHomemMaisVelho)
        else:
            if Idade > IdadeHomemMaisVelho:
                IdadeHomemMaisVelho = Idade
                NomeHomemMaisVelho = Nome
                print(NomeHomemMaisVelho)
    elif Sexo.upper() == 'F':
        if Idade > 21:
            MulheresMaiores += 1
        elif Idade < 21:
            MulheresMenores += 1
print('A média de idade dessas 4 pessoas é: {}'.format(IdadeMédia / 4))
print('O homem mais velho é o {} que tem {} anos'.format(NomeHomemMaisVelho, IdadeHomemMaisVelho))
print('Existem {} mulheres com mais de 21 anos e {} mulheres com menos de 21 anos'.format(MulheresMaiores, MulheresMenores))


