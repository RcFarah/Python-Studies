# Exercício #038

numero1 = int(input('Digite o valor do primeiro número: '))
numero2 = int(input('Digite o valor do segundo número: '))

if numero1 > numero2:
    print('O número {} é maior que o número {}!'.format(numero1, numero2))
elif numero2 > numero1:
    print('O número {} é maior que o número {}!'.format(numero2, numero1))
elif numero1 == numero2:
    print('Os dois número são IGUAIS.')
