# Desafio #007

aluno = str(input('Digite o nome do aluno: ')).strip().title()
nota1 = float(input('Digite a primeira nota do aluno {}: '.format(aluno)))
nota2 = float(input('Digite a segunda nota do aluno {}:'.format(aluno)))
medianota = (nota1 + nota2) / 2
print('A média do aluno {} foi de: {}'.format(aluno, medianota))
