n = input('digite algo: ')
print('o tipo primitivo de {} é '.format(n), type(n))
print('é numérico? {}'.format(n.isnumeric()))
print('é afabético', n.isalpha())
print('é alfanumérico', n.isalnum())
print('so tem espaço', n.isspace())