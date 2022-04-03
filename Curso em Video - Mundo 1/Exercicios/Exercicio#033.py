# Desafio #033

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('NÃO REPITA NÚMEROS!')
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
terceiro_numero = int(input('Digite o terceiro número: '))
if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    print('O maior número é: {}'.format(primeiro_numero))
    if segundo_numero > terceiro_numero:
        print('O menor número é: {}'.format(terceiro_numero))
    if segundo_numero < terceiro_numero:
        print('O menor número é: {}'.format(segundo_numero))
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print('O maior número é: {}'.format(segundo_numero))
    if primeiro_numero > terceiro_numero:
        print('O menor número é: {}'.format(terceiro_numero))
    if terceiro_numero > primeiro_numero:
        print('O menor número é: {}'.format(primeiro_numero))
elif terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
    print('O maior número é? {}'.format(terceiro_numero))
    if primeiro_numero > segundo_numero:
        print('O menor número é: {}'.format(segundo_numero))
    if segundo_numero > primeiro_numero:
        print('O menor número é: {}'.format(primeiro_numero))
