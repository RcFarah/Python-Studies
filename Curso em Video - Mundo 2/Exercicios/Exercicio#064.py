# Exercicio #064

# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 0, que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).

contador = 0
soma_geral = []
resultado_final = 0

numero = int(input('Digite primeiro número: '))
soma_geral.append(numero)

while numero != 0:
    contador += 1
    numero = int(input('Digite o próximo número a ser somado (para sair digite 0): '))
    soma_geral.append(numero)
    resultado_final = sum(soma_geral)


print('\nVocê digitou {} valores.\n'
      'A soma de todos os valores é de: {}'.format(contador, resultado_final))

# OU

# contador = 0
# soma = 0
# resultado_final = 0

# numero = int(input('Digite primeiro número: '))
# soma = numero

# while numero != 0:
#     contador += 1
#     numero = int(input('Digite o próximo número a ser somado (para sair digite 0): '))
#     soma += numero
#     resultado_final = soma


# print('\nVocê digitou {} valores.\n'
#       'A soma de todos os valores é de: {}'.format(contador, resultado_final))
