# Desafio #009

# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Digite um número, para ver sua tabuada:'))
x1 = numero * 1
x2 = numero * 2
x3 = numero * 3
x4 = numero * 4
x5 = numero * 5
x6 = numero * 6
x7 = numero * 7
x8 = numero * 8
x9 = numero * 9
x10 = numero * 10
print('--' * 12)
print('A tabuada do número {} é:\n'
      '{} x 1 = {}\n'
      '{} x 2 = {}\n'
      '{} x 3 = {}\n'
      '{} x 4 = {}\n'
      '{} x 5 = {}\n'
      '{} x 6 = {}\n'
      '{} x 7 = {}\n'
      '{} x 8 = {}\n'
      '{} x 9 = {}\n'
      '{} x 10 = {}'.format(numero, numero, x1, numero, x2, numero, x3, numero, x4, numero, x5, numero, x6, numero, x7,
                            numero, x8, numero, x9, numero, x10))
print('--' * 12)
