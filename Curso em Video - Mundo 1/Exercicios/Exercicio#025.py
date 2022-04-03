# Desafio #025

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome_completo = str(input('Qual o seu nome completo? : ')).strip().title()
nome_dividido = nome_completo.split()
print('Seu nome possui Silva? : {}'.format('Silva' in nome_dividido))
