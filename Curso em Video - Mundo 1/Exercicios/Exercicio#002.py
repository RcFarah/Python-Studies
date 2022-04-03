# Desafio #002

# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = str(input("Digite seu nome: ")).strip().title()
print('Olá {}, prazer te conhecer!'.format(nome))
