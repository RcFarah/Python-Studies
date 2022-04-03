# Exercicio #050

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

soma = 0
contador = 0

for pergunta in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Você informou {} número(s) par(es) e a soma deles foi: {}'.format(contador, soma))
