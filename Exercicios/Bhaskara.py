from math import sqrt

valor_a = int(input('Digite o valor de A: '))
valor_b = int(input('Digite o valor de B: '))
valor_c = int(input('Digite o valor de C: '))
delta = (valor_b ** 2) - (4 * valor_a * valor_c)
if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    bhaskara = ((- 1 * valor_b) + sqrt(delta)) / (2 * valor_a)
    print('a raiz desta equação é {}'.format(bhaskara))
elif delta > 0:
    bhask_positivo = ((- 1 * valor_b) + sqrt(delta)) / (2 * valor_a)
    bhask_negativo = ((- 1 * valor_b) - sqrt(delta)) / (2 * valor_a)
    if bhask_positivo == bhask_negativo:
        print('as raízes da equação são {} e {}'.format(bhask_negativo, bhask_negativo))
    elif bhask_positivo < bhask_negativo:
        ordem_crescente = [bhask_negativo, bhask_positivo]
        lista_crescente = ordem_crescente.sort()
        print('as raízes da equação são {} e {}'.format(lista_crescente[0], lista_crescente[1]))
