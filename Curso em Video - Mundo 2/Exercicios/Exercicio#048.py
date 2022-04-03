# Exercicio #048

# Faça um programa que calcule a SOMA entre todos os número ímpares múltiplos de 3 e que se encontram
# no intervalo de 1 até 500

soma = 0
cont = 0

for contador in range(1, 501, 2):
    if contador % 3 == 0:
        cont = cont + 1
        soma = soma + contador
print('A soma dos {} números é de: {}'.format(cont, soma))
