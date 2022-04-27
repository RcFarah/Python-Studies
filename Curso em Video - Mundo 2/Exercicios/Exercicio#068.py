# Exericio #068

# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import choice

numeros_pc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador = contador_vitorias = 0

print('Vamos jogar Par ou Ímpar?\n'
      '(O programa só para quando você: Perder ou jogar um número negativo)')

while True:
    print('-' * 25)
    numero_jogador = int(input('Qual número quer jogar: '))
    if numero_jogador < 0:
        print('Programa finalizado.')
        break
    par_impar = str(input('Quer Par (P) ou Ímpar (I): ')).strip().upper()
    print('-' * 25)

    jogada_pc = choice(numeros_pc)
    soma = numero_jogador + jogada_pc
    divisao = soma % 2

    if par_impar == 'I':
        contador += 1
        if divisao == 0:
            print('Você jogou: {}\n'
                  'Computador jogou: {}\n'
                  'Total: {} (PAR)\n'
                  'Você \033[31mPERDEU\033[m'.format(numero_jogador, jogada_pc, soma), end='\n \n')
            print('Você tentou: {} vez(es)\n'
                  'Ganhou: {} vez(es)'.format(contador, contador_vitorias))
            break

        else:
            print('Você jogou: {}\n'
                  'Computador jogou: {}\n'
                  'Total: {} (ÍMPAR)\n'
                  'Você \033[34mGANHOU\033[m'.format(numero_jogador, jogada_pc, soma), end='\n \n')
            contador_vitorias += 1

    elif par_impar == 'P':
        contador += 1
        if divisao != 0:
            print('Você jogou: {}\n'
                  'Computador jogou: {}\n'
                  'Total: {} (ÍMPAR)\n'
                  'Você \033[31mPERDEU\033[m'.format(numero_jogador, jogada_pc, soma), end='\n \n')
            print('Você tentou: {} vez(es)\n'
                  'Ganhou: {} vez(es)'.format(contador, contador_vitorias))
            break

        else:
            print('Você jogou: {}\n'
                  'Computador jogou: {}\n'
                  'Total: {} (PAR)\n'
                  'Você \033[34mGANHOU\033[m'.format(numero_jogador, jogada_pc, soma), end='\n \n')
            contador_vitorias += 1

    else:
        print('OPÇÃO INVÁLIDA')
