# Exercício #038

# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numero1 = int(input('Digite o valor do primeiro número: '))
numero2 = int(input('Digite o valor do segundo número: '))

if numero1 > numero2:
    print('O número {} é maior que o número {}!'.format(numero1, numero2))
elif numero2 > numero1:
    print('O número {} é maior que o número {}!'.format(numero2, numero1))
elif numero1 == numero2:
    print('Os dois número são IGUAIS.')
