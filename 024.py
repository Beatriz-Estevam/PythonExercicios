city = str(input('Cidade: '))
citySplit = city.split()
PrimeiroNomeCity = citySplit[0]
cityUpper = PrimeiroNomeCity.upper()
print('A cidade {} começa com "Santo": {}'.format(city, 'SANTO' in cityUpper))
