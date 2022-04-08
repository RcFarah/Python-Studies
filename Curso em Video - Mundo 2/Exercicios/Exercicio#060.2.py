# Exercicio #060.2

# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# UTILIZANDO FOR

numero = int(input('Digite o número que deseja descobrir o fatorial: '))
contador = numero
fatorial = 1

print('Calculando {}! = '.format(numero), end='')

for contador in range(numero, 0, -1):
    print(contador, ' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1
print(fatorial)
