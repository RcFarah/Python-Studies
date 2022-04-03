# Exercicio #037

# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))

opcao = int(input('Para qual base deseja converter?\n'
                  'Digite 1 para: \033[1;31mBinária\033[m\n'
                  'Digite 2 para: \033[1;31mOctal\033[m\n'
                  'Digite 3 para: \033[1;31mHexadecimal\033[m\n'
                  ''))

if opcao == 1:
    numero_trans = bin(numero)
    print('O número {} passa a ser: {}'.format(numero, numero_trans[2:]))
elif opcao == 2:
    numero_trans = oct(numero)
    print('O número {} passa a ser: {}'.format(numero, numero_trans[2:]))
elif opcao == 3:
    numero_trans = hex(numero)
    print('O número {} passa a ser: {}'.format(numero, numero_trans[2:]))
