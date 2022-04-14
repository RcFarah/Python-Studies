# Exercicio #065

# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
# ou não continuar a digitar valores.

# Declarando variáveis
numero = int(input('Digite um número: '))
numero_list = [numero]
continua_para = int(input('Deseja continuar a inserir mais números?\n'
                          '[1] Para \033[34mCONTINUAR\033[m\n'
                          '[2] Para \033[31mPARAR\033[m\n'))
media_all_num = sum(numero_list) / len(numero_list)
soma_all_num = sum(numero_list)
contador = 1

# Declarando condição
while continua_para == 1:
    numero = int(input('Digite outro número: '))
    continua_para = int(input('Deseja continuar a inserir mais números?\n'
                              '[1] Para \033[34mCONTINUAR\033[m\n'
                              '[2] Para \033[31mPARAR\033[m\n'))
    numero_list.append(numero)
    soma_all_num = sum(numero_list)
    media_all_num = soma_all_num / len(numero_list)
    contador += 1

# Print do resultado que o programa espera
print('Você digitou {} número(s)\n'
      'A soma de todos esses números é igual a: {}\n'
      'A média de todos esses número é igual a: {}\n'
      'O menor número é: {}\n'
      'O maior número é: {}'.format(contador, soma_all_num, media_all_num, numero_list[0], numero_list[-1]))
