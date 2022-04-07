# Exercicio #059

#  Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

resposta = 0

primeiro_num = float(input('Digite o primeiro valor: '))
segundo_num = float(input('Digite o segundo valor: '))
opcao = int(input('Escolha uma opção:\n'
                  '[1] SOMAR\n'
                  '[2] MULTIPLICAR\n'
                  '[3] DIVIDIR\n'
                  '[4] SUBTRAIR\n'
                  '[5] NOVOS NÚMEROS\n'
                  '\033[31m[6] SAIR\033[m\n'))

while opcao != 6:
    if opcao == 1:
        resposta = primeiro_num + segundo_num
        print('A soma dos dois valores foi: \033[34m{}\033[m'.format(resposta), end='\n \n')
    elif opcao == 2:
        resposta = primeiro_num * segundo_num
        print('A multiplicação dos dois valores foi: \033[34m{}\033[m'.format(resposta), end='\n \n')
    elif opcao == 3:
        resposta = primeiro_num / segundo_num
        print('A divisão dos dois valores foi: \033[34m{}\033[m'.format(resposta), end='\n \n')
    elif opcao == 4:
        resposta = primeiro_num - segundo_num
        print('A subtração dos dois números foi: \033[34m{}\033[m'.format(resposta), end='\n \n')
    elif opcao == 5:
        primeiro_num = float(input('Digite o primeiro valor: '))
        segundo_num = float(input('Digite o segundo valor: '))
    else:
        print('OPÇÃO INVÁLIDA!')
    opcao = int(input('Escolha uma opção:\n'
                      '[1] SOMAR\n'
                      '[2] MULTIPLICAR\n'
                      '[3] DIVIDIR\n'
                      '[4] SUBTRAIR\n'
                      '[5] NOVOS NÚMEROS\n'
                      '\033[31m[6] SAIR\033[m\n'))

print('Você saiu do programa com sucesso!')
