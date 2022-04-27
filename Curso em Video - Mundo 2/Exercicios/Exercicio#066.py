# Exercico #066

# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

numero = int(input('Digite o primeiro número a ser somado: '))
contador = 1
soma = numero

while True:
    numero = int(input('Digite o próximo número a ser somado (para sair digite 999): '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print('Você digitou {} números.\n'
      'A soma entre esses números é: {}'.format(contador, soma))
