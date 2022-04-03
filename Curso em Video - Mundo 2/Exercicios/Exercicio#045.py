# Exercicio #045

# Crie um programa que faça o computador jogar Pedra, Papel e Tesoura com você.

import random

lista_maquina = ['Pedra', 'Papel', 'Tesoura']
jogar = int(input('Olá, vamos jogar Pedra, Papel e Tesoura?\n'
                  '(1) para SIM\n'
                  '(2) para NÃO\n'
                  'Digite: '))

if jogar == 1:
    jogada_usuario = int(input('Okay, então partiu diversão!\n'
                               'Para começar, digite:\n'
                               '(1) para Pedra\n'
                               '(2) para Papel\n'
                               '(3) para Tesoura.\n'
                               'Boa sorte!\n'))
    escolha_maquina = random.choice(lista_maquina)

    if jogada_usuario == 1:
        jogada_usuario = 'Pedra'
        if escolha_maquina == 'Pedra':
            print('Você jogou: {}\n'
                  'Máquina jogou: {}\n'
                  'EMPATE'.format(jogada_usuario, escolha_maquina))
        elif escolha_maquina == 'Papel':
            print('Você jogou: {}\n'
                  'Máquina jogou: {}\n'
                  'MÁQUINA GANHOU!'.format(jogada_usuario, escolha_maquina))
        elif escolha_maquina == 'Tesoura':
            print('Você jogou: {}\n'
                  'Máquina jogou: {}\n'
                  'VOCÊ GANHOU!'.format(jogada_usuario, escolha_maquina))

    if jogada_usuario == 2:
        jogada_usuario = 'Papel'
        if escolha_maquina == 'Pedra':
            print('Você jogou: {}\n'
                  'Máquina jogou: {}\n'
                  'VOCÊ GANHOU!'.format(jogada_usuario, escolha_maquina))
        elif escolha_maquina == 'Papel':
            print('Você jogou: {}\n'
                  'Máquina jogou: {}\n'
                  'EMPATE!'.format(jogada_usuario, escolha_maquina))
        elif escolha_maquina == 'Tesoura':
            print('Você jogou: {}\n'
                  'Máquina jogou: {}\n'
                  'MÁQUINA GANHOU!'.format(jogada_usuario, escolha_maquina))

    if jogada_usuario == 3:
        jogada_usuario = 'Tesoura'
        if escolha_maquina == 'Pedra':
            print('Você jogou: {}\n'
                  'Máquina jogou: {}\n'
                  'MÁQUINA GANHOU!'.format(jogada_usuario, escolha_maquina))
        elif escolha_maquina == 'Papel':
            print('Você jogou: {}\n'
                  'Máquina jogou: {}\n'
                  'VOCÊ GANHOU!'.format(jogada_usuario, escolha_maquina))
        elif escolha_maquina == 'Tesoura':
            print('Você jogou: {}\n'
                  'Máquina jogou: {}\n'
                  'EMPATE!'.format(jogada_usuario, escolha_maquina))
else:
    print('Okay, então MORRE, DIABO.')
