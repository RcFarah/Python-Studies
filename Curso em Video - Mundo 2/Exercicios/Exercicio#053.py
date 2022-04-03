# Exercicio #053

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juncao = ''.join(palavras)
inverso = ''

for letras in range(len(juncao) - 1, -1, -1):
    inverso += juncao[letras]

print('{} x {}'.format(juncao, inverso))

if inverso == juncao:
    print('Temos um palíndromo!')

else:
    print('Não temos um palíndromo.')


# OU

# frase = str(input('Digite uma frase: ')).strip().upper()
# palavras = frase.split()
# juncao = ''.join(palavras)
# inverso = junto[::-1}
#
# print('{} x {}'.format(juncao, inverso))
#
# if inverso == juncao:
#     print('Temos um palíndromo!')
#
# else:
#     print('Não temos um palíndromo.')
