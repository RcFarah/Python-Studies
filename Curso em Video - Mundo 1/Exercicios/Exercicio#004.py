# Desafio #004

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está somente em maiúsculas? {}'.format(algo.isupper()))
print('Está somente em minúsculas? {}'.format(algo.islower()))
print('Está capitalizada? {}'.format(algo.istitle()))
