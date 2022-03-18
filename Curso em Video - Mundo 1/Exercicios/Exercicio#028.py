# Desafio #028
import random

lista = [0, 1, 2, 3, 4, 5]
sort_lista = random.choice(lista)
print('-=' * 10)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=' * 10)
resposta = int(input('Em que número eu pensei? '))
print('Eu pensei no número {}, você respondeu {}.'.format(sort_lista, resposta))
if resposta == sort_lista:
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você não acertou... Tente novamente.')
