sexo = str(input('Qual o seu sexo [F/M]: ')).upper().strip()
while sexo != 'F' and  sexo != 'M':
    print('\033[31m!!!O valor digitado não é computável!!!\033[m')
    print('Digite \033[35m[F] para sexo feminino\033[m e \033[34m[M] para sexo masculino\033[m')
    sexo = str(input('Qual o seu sexo: ')).upper().strip()
if sexo == 'M':
    print('Você é do sexo \033[34mMasculino\033[m')
else:
    print('Você é do sexo \033[35mfeminino')

