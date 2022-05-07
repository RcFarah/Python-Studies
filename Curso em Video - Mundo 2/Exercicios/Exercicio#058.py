# Exercicio #058

# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

lista_pc_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tentativas = 0
numero_pensado_pc = random.choice(lista_pc_numeros)
resposta = 999

while resposta != numero_pensado_pc:
    print('Pensei em um número de 0 a 10, tente adivinhar qual número eu pensei!')
    resposta = int(input('\nQual número você acha que a máquina pensou? '))
    tentativas += 1
    print('ERROUUUUU.\n'
          'Eu pensei no número \033[31m{}\033[m, você disse que eu pensei no \033[33m{}\033[m\n'
          .format(numero_pensado_pc, resposta),
          '_' * 50, end='\n \n')

print('PARABÉNS!\n'
      'Você acertou!\n'
      'Você precisou de \033[34m{}\033[m tentativa(s).'.format(tentativas), end='\n \n')
