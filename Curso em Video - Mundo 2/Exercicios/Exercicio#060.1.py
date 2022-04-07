# Exercicio #060

# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# UTILIZANDO WHILE

numero = int(input('Digite o número que deseja descobrir o fatorial: '))
multiplicador = numero - 1
resultado = 0
resultado_final = 0

while multiplicador > 0:
    resultado = numero * multiplicador
    multiplicador -= 1
    resultado_final = resultado * multiplicador
    print(resultado_final)


print(resultado_final)
