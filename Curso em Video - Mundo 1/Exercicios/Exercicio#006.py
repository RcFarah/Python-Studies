# Desafio #006

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = float(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizquadrada = num ** 0.5
print('Analisando o número {}, conclui-se que:\n'
      'Seu dobro é: {}\n'
      'Seu triplo é: {}\n'
      'Sua raiz quadrada é: {}'.format(num, dobro, triplo, raizquadrada))

# CASO QUEIRA, PODE IMPORTAR A BIBLIOTECA MATH E USAR O .sqrt PARA FAZER A RAIZ QUADRADA
# FICANDO DA SEGUNTE FORMA
# from math import sqrt
# numero = float(input('Digite um número: '))
# dobro = numero * 2
# triplo = numero * 3
# raizquadrada = math.sqrt(numero)
# print('Analisando o número {}, conclui-se que:\n'
#       'Seu dobro é: {}\n'
#       'Seu triplo é: {}\n'
#       'Sua raiz quadrada é: {}'.format(numero, dobro, triplo, raizquadrada))
