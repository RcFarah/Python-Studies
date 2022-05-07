# Exercicio #071 # INCREMENTADO POR MIM

# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from time import sleep
import keyboard
import random

tempo_sleep = [0.5, 1, 1.5, 2, 2.5, 3]

# Inicialização da máquina
print('-' * 15, 'BEM VINDO AO', '-' * 15)
print('{:-^44}'.format(' BANCO GREMLIN '))
print('\n \nApós inserir seu cartão na máquina, aperte ESPAÇO para continuar.')

# Condição de partida da máquina
keyboard.wait('space')
print('\nPROCESSANDO...')
sleep(random.choice(tempo_sleep))

print('\nRETIRE O CARTÃO.')

# Opções Bancárias da Máquina
opcao = ' '

while opcao not in ['1', '2', '3', '4']:
    opcao = str(input('\nSELECIONE UMA OPÇÃO:\n'
                      '\033[32m[1] DEPÓSITO\033[m\n'
                      '\033[32m[2] SAQUE\033[m\n'
                      '\033[32m[3] SALDO/EXTRATO\033[m\n'
                      '\033[32m[4] POUPANÇA\033[m\n')).strip()[0]
    if opcao in ['1', '2', '3', '4']:
        break
    if opcao not in ['1', '2', '3', '4']:
        print('OPÇÃO INVÁLIDA.\nTENTE NOVAMENTE.')
print('\nPROCESSANDO...\n')
sleep(random.choice(tempo_sleep))


# Caminho para as diferentes respostas das opções

# Opção de depósito
if opcao == '1':
    print('Para continuar com o depósito, favor insira o envelope com o dinheiro na abertura ao lado.')
    print('Ao inserir, favor aperte ESPAÇO.')

    keyboard.wait('space')
    print('\nPROCESSANDO...\n')
    sleep(random.choice(tempo_sleep))

    cpf = str(input('Favor insira o CPF do destinatário (sem Pontos e Traços): ')).strip()
    print('O CPF está correto? \033[31m{}\033[m'.format(cpf))

    resposta = ' '

    while resposta != 'S':
        resposta = str(input('[S/N}: ')).strip().upper()[0]
        if resposta == 'S':
            print('\nDEPÓSITO EFETUADO.\n')
            break
        elif resposta == 'N':
            cpf = str(input('Favor insira o CPF do destinatário (sem Pontos e Traços): ')).strip()

# Opção do DESAFIO
elif opcao == '2':
    print('Notas disponíveis para saque:R$200, R$100, R$50, R$20, R$10, R$5\n')
    prosseguir = ' '

    # Se a pessoa quiser sair do saque
    while prosseguir not in 'NS':
        prosseguir = str(input('DESEJA PROSSEGUIR? [S/N}: ')).strip().upper()[0]
        if prosseguir == 'S':
            print('PROSSEGUINDO.')
            break
        elif prosseguir == 'N':
            break

    # Prosseguindo com o Saque
    if prosseguir == 'S':
        valor_saque = int(input('INSIRA O VALOR DO SAQUE: R$'))
        total = valor_saque
        nota = 200
        total_notas = 0

        # Descobrindo quantas notas de cada serão impressas
        while True:
            if total >= nota:
                total -= nota
                total_notas += 1
            else:
                if total_notas > 0:
                    print('Total de {} notas de R${}'.format(total_notas, nota))
                total_notas = 0
                if nota == 200:
                    nota = 100
                elif nota == 100:
                    nota = 50
                elif nota == 50:
                    nota = 20
                elif nota == 20:
                    nota = 5
                if total == 0:
                    break
    print('\nENCERRANDO SESSÃO.\n')

# Opção de Saldo
elif opcao == '3':
    saldo = random.randint(-1000, 100000)
    if saldo < 0:
        print('Seu saldo devedor é de: -R${:.2f}'.format(saldo))
    else:
        print('Seu saldo atual é de: R${:.2f}'.format(saldo))
    sleep(1.5)
    print('\nFINALIZANDO SESSÃO.\n')
    sleep(1.0)

# Opção de Poupança
elif opcao == '4':
    # Declarando variaveis que utilizarei na poupança
    saldo = random.randint(50, 10000)
    rendimento_poup = random.uniform(0.5, 2.5)
    print('Seu saldo atual na poupança é de: R${:.2f}\n'.format(saldo))
    print('A poupança atualmente rende {:.2f}% ao mês.\n'.format(rendimento_poup))

    print('Deseja fazer uma projeção do seu saldo na poupança?')
    resposta = ' '
    while resposta != 'S' or 'N':  # Caso a resposta esja diferente de alguma aceita, repete a pergunta

        resposta = str(input('[S/N}: ')).strip().upper()[0]  # Recebe a resposta

        if resposta == 'S':  # Caso a resposta seja Sim, ele fará tal coisa

            meses_a_frente = int(input('Quantos meses a frente deseja projetar o saldo?\n'
                                       'Opções:\n'
                                       '[3] Meses\n'
                                       '[6] Meses\n'
                                       '[12] Meses\n'
                                       '[24] Meses\n'))

            # Cálculo do rendimento da poupança
            rend_mensal = rendimento_poup / 100
            somar_no_saldo = saldo * rend_mensal * meses_a_frente
            novo_saldo = saldo + somar_no_saldo
            print('\nSeu saldo daqui a {} meses, será de R${:.2f}\n'.format(meses_a_frente, novo_saldo))
            break  # Sai da projeção

        else:
            break  # não faz nenhuma projeção

    print('Deseja adicionar ou resgatar dinheiro da poupança?')
    resposta1 = ' '

    while resposta1 != 'S' or 'N':  # Caso a resposta esja diferente de alguma aceita, repete a pergunta

        resposta1 = str(input('[S/N}: ')).strip().upper()[0]  # Recebe a resposta

        if resposta1 == 'S':  # Caso a resposta seja Sim, ele fará tal coisa

            resposta2 = ' '
            while resposta2 != '1' or '2':  # Caso a resposta esja diferente de alguma aceita, repete a pergunta

                resposta2 = str(input('\nESCOLHA A OPÇÃO:\n'
                                      '\033[32m[1] Adicionar\033[m\n'
                                      '\033[31m[2] Remover\033[m')).strip().upper()[0]  # Recebe a resposta

                if resposta2 == '1':  # Caso a resposta seja Adicionar

                    # Indico novas variaveis úteis
                    valor_add = float(input('\nQuantos R$ deseja adicionar a sua poupança: R$'))
                    novo_saldo = saldo + valor_add
                    saldo = novo_saldo  # Saldo recebe o novo saldo

                    # Printo o novo saldo
                    print('\nSeu novo saldo na poupança é de: R${:.2f}\n'.format(novo_saldo))

                    print('Deseja fazer uma nova projeção do seu saldo na poupança?')
                    resposta3 = ' '

                    while resposta3 != 'S' or 'N':  # Caso a resposta esja diferente de alguma aceita, repete a pergunta
                        resposta3 = str(input('[S/N}: ')).strip().upper()[0]  # Recebe a resposta
                        if resposta3 == 'S':  # Caso a resposta seja Sim
                            meses_a_frente = int(input('\nQuantos meses a frente deseja projetar o saldo?\n'
                                                       'Opções:\n'
                                                       '[3] Meses\n'
                                                       '[6] Meses\n'
                                                       '[12] Meses\n'
                                                       '[24] Meses\n'))

                            # Cálculo do rendimento da poupança
                            rend_mensal = rendimento_poup / 100
                            somar_no_saldo = saldo * rend_mensal * meses_a_frente
                            novo_saldo = saldo + somar_no_saldo
                            print('Seu saldo daqui a {} meses, será de R${:.2f}'.format(meses_a_frente, novo_saldo))
                            sleep(1.5)
                            print('-' * 30, 'FINALIZANDO SESSÃO.', '-' * 30)
                            sleep(2)
                            break
                        else:
                            sleep(1.5)
                            print('-' * 30, 'FINALIZANDO SESSÃO.', '-' * 30)
                            sleep(2)
                            break
                    else:
                        sleep(1.5)
                        print('-' * 30, 'FINALIZANDO SESSÃO.', '-' * 30)
                        sleep(2)
                    break

                elif resposta2 == '2':  # Caso a resposta seja Remover
                    valor_remove = float(input('Quantos R$ deseja remover da sua poupança: R$'))
                    novo_saldo = saldo - valor_remove
                    print('Seu novo saldo na poupança é de: R${:.2f}'.format(novo_saldo))
                    print('Deseja fazer uma nova projeção do seu saldo na poupança?')
                    resposta3 = ' '
                    while resposta3 != 'S' or 'N':  # Caso a resposta esja diferente de alguma aceita, repete a pergunta
                        resposta3 = str(input('[S/N}: ')).strip().upper()[0]
                        if resposta3 == 'S':  # Caso a resposta seja Sim
                            meses_a_frente = int(input('Quantos meses a frente deseja projetar o saldo?\n'
                                                       'Opções:\n'
                                                       '[3] Meses\n'
                                                       '[6] Meses\n'
                                                       '[12] Meses\n'
                                                       '[24] Meses\n'))

                            # Cálculo do rendimento da poupança
                            rend_mensal = rendimento_poup / 100
                            somar_no_saldo = saldo * rend_mensal * meses_a_frente
                            novo_saldo = saldo + somar_no_saldo
                            print('Seu saldo daqui a {} meses, será de R${:.2f}'.format(meses_a_frente, novo_saldo))
                            break
                        else:
                            break
                    sleep(1.5)
                    print('-' * 30, 'FINALIZANDO SESSÃO.', '-' * 30)
                    sleep(2)
                    break
        break

print('\n')
print('-' * 30, 'SESSÃO FINALIZADA', '-' * 30)
