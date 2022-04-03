# Desafio #027

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

nome = str(input('Escreva seu nome completo: ')).strip().title()
nome_dividido = nome.split()
print('Seu primeiro nome é: {}\n'
      'Seu último nome é: {}'.format(nome_dividido[0], nome_dividido[-1]))
