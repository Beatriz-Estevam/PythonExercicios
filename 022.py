NomeCompleto = str(input('Digite seu nome completo: '))
print('O nome {} com todas as letras maiúsculas fica {}'.format(NomeCompleto, NomeCompleto.upper()))
print('O nome {} com todas as letras miúsculas fica {}'.format(NomeCompleto, NomeCompleto.lower()))
NomeCompletoSemEspaço = NomeCompleto.replace(' ','')
print('O nome {} possui {} letras'.format(NomeCompleto, len(NomeCompletoSemEspaço)))
PrimeiroNome = NomeCompleto.split()
print('O primeiro nome de {} é {} e possui {} letras'.format(NomeCompleto, PrimeiroNome[0], len(PrimeiroNome[0])))
