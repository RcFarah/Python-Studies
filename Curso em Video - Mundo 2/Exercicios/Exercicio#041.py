# Exercicio #041

# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

nome_aluno = str(input('Digite o nome do(a) aluno(a): ')).strip().title()
idade = int(input('Digite a idade do(a) aluno(a): '))

if idade < 9:
    print('O(A) aluno(a) {} é da categoria: Mirim.'.format(nome_aluno))
elif idade < 14:
    print('O(A) aluno(a) {} é da categoria: Infantil.'.format(nome_aluno))
elif idade < 19:
    print('O(A) aluno(a) {} [e da categoria: Junior.'.format(nome_aluno))
elif idade < 20:
    print('O(A) aluno(a) é da categoria: Sênior.'.format(nome_aluno))
else:
    print('O(A) aluno(a) é da categoria: Master.'.format(nome_aluno))
