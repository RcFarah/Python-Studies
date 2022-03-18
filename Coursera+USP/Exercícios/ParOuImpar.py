numero = int(input('Digite um número qualquer para saber se ele é Par ou Ímpar: '))
divisão = numero % 2
if divisão == 0:
    print('par')
else:
    print('ímpar')
