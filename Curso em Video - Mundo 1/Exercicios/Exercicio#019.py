# Desafio #019

import random
aluno1 = str(input('Digite o nome de um aluno: ')).strip().title()
aluno2 = str(input('Digite o nome de mais um aluno: ')).strip().title()
aluno3 = str(input('Digite o nome de mais um aluno: ')).strip().title()
aluno4 = str(input('Digite o nome de mais um aluno: ')).strip().title()
aluno5 = str(input('Digite o nome de mais um aluno: ')).strip().title()
alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
print('O aluno sorteado entre os 5 foi: {}'.format(random.choice(alunos)))
