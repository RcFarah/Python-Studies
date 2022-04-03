# Exercício #040

# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

aluno = str(input('Digite o nome do Aluno: ')).title().strip()
nota1 = int(input('Digite a primeira nota de {}: '.format(aluno)))
nota2 = int(input('Digite a segunda nota de {}: '.format(aluno)))
media = (nota1 + nota2) / 2

if media >= 7.0:
    print('O(A) aluno(a) {} foi APROVADO.\n'
          'Sua média foi: {}'.format(aluno, media))
if 5.0 <= media < 6.9:
    print('O(A) aluno(a) {} está de RECUPERAÇÃO.\n'
          'Sua média foi: {}'.format(aluno, media))
if media < 5.0:
    print('O(A) aluno(a) {} foi REPROVADO.\n'
          'Sua média foi: {}'.format(aluno, media))
