# Desafio #018

import math

angulo = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo {}\nTem o SENO de: {:.2f}\nTem o COSSENO de: {:.2f}\nTem a TANGENTE de: {:.2f}'.format(angulo, seno,
                                                                                                     cosseno, tangente))
