# Exercicio #052

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número inteiro: '))
divisoes = 0

for divisao in range(1, numero + 1):
    if numero % divisao == 0:
        print('\033[34m', end=' ')
        divisoes += 1
    else:
        print('\033[31m', end=' ')
    print(divisao, end='')

if divisoes == 2:
    print('\033[m\nO número {} é PRIMO!'.format(numero))

else:
    print('\033[m\nO número {} NÃO É PRIMO.'.format(numero))
