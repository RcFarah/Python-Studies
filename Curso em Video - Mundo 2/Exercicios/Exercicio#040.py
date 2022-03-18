# Exercício #040

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
