numero = int(input('Digite um numer maior que 1: '))

fator = 2
multiplicidade = 0

while numero > 1:
    while numero % fator == 0:
        multiplicidade = multiplicidade + 1
        numero = numero / fator
    if multiplicidade > 0:
        print('Fator: {} - Multiplicidade: {}'.format(fator, multiplicidade))
    fator = fator + 1
    multiplicidade = 0
