# Exercicio #069

#  Crie um programa que leia a IDADE e o SEXO de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
#  se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cont = 0
quant_homem = 0
quant_mulher_20_under = 0
mais_18 = 0

while True:
    print('-' * 30)
    print('CADASTRO INICIADO.')
    print('-' * 30)

    nome = str(input('Digite o nome completo da pessoa a ser cadastrada: ')).strip().title()
    idade = int(input('Digite a idade da pessoa a ser cadastrada: '))
    sexo = str(input('Escolha uma opção para o sexo da pessoa:\n'
                     '\033[34m(M)\033[m Para Masculino\n'
                     '\033[32m(F)\033[m Para Feminino\n'
                     '\033[35m(O)\033[m Para Outro\n')).strip().upper()

    if sexo not in ['M', 'F', 'O']:
        print('OPÇÃO INVÁLIDA.\nTENTE NOVAMENTE')
        while sexo not in ['M', 'F', 'O']:
            sexo = str(input('Escolha uma opção para o sexo da pessoa:\n'
                             '\033[34m(M)\033[m Para Masculino\n'
                             '\033[32m(F)\033[m Para Feminino\n'
                             '\033[35m(O)\033[m Para Outro\n')).strip().upper()

    if sexo == 'M':
        quant_homem += 1
    elif sexo == 'F':
        if idade < 20:
            quant_mulher_20_under += 1

    if idade > 18:
        mais_18 += 1

    cont += 1

    continuar = str(input('Deseja continuar? (S/N): ')).upper().strip()
    if continuar != 'S':
        print('OPÇÃO INVÁLIDA.\nTENTE NOVAMENTE.')
        while continuar not in 'NS':
            continuar = str(input('Deseja continuar? (S/N): ')).upper().strip()
            if continuar == 'N':
                break
        if continuar == 'N':
            print('-' * 25)
            print('ENCERRANDO PROGRAMA.')
            print('-' * 25)
            break
    elif continuar == 'N':
        print('-' * 25)
        print('ENCERRANDO PROGRAMA.')
        print('-' * 25)
        break


print('Ao todo foram cadastradas {} pessoas.\n'
      'Dentre elas:\n'
      '{} maiores que 18 anos\n'
      '{} mulheres abaixo dos 20 anos\n'
      '{} homens'.format(cont, mais_18, quant_mulher_20_under, quant_homem))
