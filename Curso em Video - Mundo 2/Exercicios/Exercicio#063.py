# Exercicio #063

# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8


numero_anterior = 1
result_Fibo = 0
contador = 0

tamanho_sequencia = int(input('Digite a quantidade que deseja ver de números da Sequência de Fibonacci: '))
opcao_usuario = int(input('Escolha a opção que deseja receber:\n'
                          '[1] Mostrar contas da Sequência de Fibonacci\n'
                          '[2] Somente Sequência de Fibonacci\n'))

# Para mostrar as contas da Sequência de Fibonacci usar este:
if opcao_usuario == 1:
    while contador != tamanho_sequencia:
        print('{} + {} = {}'.format(numero_anterior, result_Fibo - numero_anterior, result_Fibo), end='\n')
        result_Fibo = result_Fibo + numero_anterior
        numero_anterior = result_Fibo - numero_anterior
        contador += 1

# Para mostrar somente o resultado da Sequência de Fibonacci usar este:
elif opcao_usuario == 2:
    while contador != tamanho_sequencia:
        print('{}'.format(result_Fibo), end=' → ')
        result_Fibo = result_Fibo + numero_anterior
        numero_anterior = result_Fibo - numero_anterior
        contador += 1


else:
    print('Opção Inválida, tente novamente.')
print('FIM')
