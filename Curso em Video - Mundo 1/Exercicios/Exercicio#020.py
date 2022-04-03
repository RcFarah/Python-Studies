# Desafio #020

# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nome_1 = str(input('Digite o nome do Primeiro Aluno: ')).strip().title()
nome_2 = str(input('Digite o nome do Segundo Aluno: ')).strip().title()
nome_3 = str(input('Digite o nome do Terceiro Aluno: ')).strip().title()
nome_4 = str(input('Digite o nome do QUarto ALuno: ')).strip().title()
lista_aleatoria = [nome_1, nome_2, nome_3, nome_4]
shuffle(lista_aleatoria)
print('A ordem de apresentação dos alunos será: {}'.format(lista_aleatoria))
