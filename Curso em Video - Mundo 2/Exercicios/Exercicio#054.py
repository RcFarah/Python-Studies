# Exercicio #054

# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

import datetime

ano_Atual = datetime.date.today().year
maior_de_idade = 0
menor_de_idade = 0

for pessoas in range(1, 9):
    ano_nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(pessoas)))
    if (ano_Atual - ano_nasc) >= 21:
        maior_de_idade += 1
    else:
        menor_de_idade += 1
print('{} pessoas já atingiram a maioridade.\n'
      '{} pessoas ainda não atingiram a maioridade.'.format(maior_de_idade, menor_de_idade))
