# Exercicio #046

# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

print('Contagem regressiva para a queima de fogos!')

for contador in range(10, -1, -1):
    print(contador)
    sleep(1)

print('FELIZ ANO NOVO!!!\n'
      'OS FOGOS ESTÃO AIII, VEJAM SÓ!')
