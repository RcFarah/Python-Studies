# Desafio #030

numero = int(input('Digite um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {}, é um número PAR.'.format(numero))
else:
    print('O número {}, é um número ÍMPAR.'.format(numero))
