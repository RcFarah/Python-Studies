# Desafio #029

import random
import time

velocidade = random.randint(1, 250)
multa = (velocidade - 80) * 7
multa_velocidade_baixa = (40 - velocidade) * 5
if velocidade > 80:
    print('Você está sendo multado por excesso de velocidade.\n'
          'Em uma area em que a velocidade máxima permitida era de 80Km/h\n'
          'o seu veículo foi registrado passando a: {}Km/h.\n'
          'Sendo assim, sua multa terá um valor de R${:.2f}\n'
          ' \n'
          'Valor da multa = (Sua Velocidade - 80) * 7'.format(velocidade, multa))
elif velocidade < 40:
    print('Você está sendo multado por baixa velocidade.\n'
          'Em uma area em que a velocidade mínima permitida era de 40Km/h\n'
          'o seu veículo foi registrado passando a: {}Km/h\n'
          'sendo assim, sua multa terá um valor de R${:.2f}\n'
          ' \n'
          'Valor da multa =  (40 - Sua Velocidade) * 5'.format(velocidade, multa_velocidade_baixa))
else:
    print('Sua velocidade foi de {}Km/h, continue respeitando os limites de velocidade!'.format(velocidade))
