from math import sqrt

coordenada_x1 = int(input('Digite o valor do primeiro X: '))
coordenada_y1 = int(input('Digite o valor do primeiro Y: '))
coordenada_x2 = int(input('Digite o valor do segundo X: '))
coordenada_y2 = int(input('Digite o valor do segundo Y: '))
distancia = sqrt(((coordenada_x1 - coordenada_x2) ** 2) + ((coordenada_y1 - coordenada_y2) ** 2))
if distancia >= 10:
    print('longe')
else:
    print('perto')
