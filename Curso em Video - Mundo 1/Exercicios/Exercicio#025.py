# Desafio #025

nome_completo = str(input('Qual o seu nome completo? : ')).strip().title()
nome_dividido = nome_completo.split()
print('Seu nome possui Silva? : {}'.format('Silva' in nome_dividido))
