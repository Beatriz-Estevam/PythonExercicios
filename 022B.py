NomeCompleto = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras MIÚSCULAS fica: {}'.format(NomeCompleto.upper()))
print('Seu nome em letras minúsculas fica: {}'.format(NomeCompleto.lower()))
print('Seu nome possui {} letras'.format(len(NomeCompleto)-NomeCompleto.count(' ')))
PrimeiroNome = NomeCompleto.split()
print('O seu primeiro nome é {} e ele possui {} letras'.format(PrimeiroNome[0], NomeCompleto.find(' ')))
