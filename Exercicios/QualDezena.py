numero = int(input('Digite um número qualquer: '))
dezena_conta_1 = numero // 10
dezena_conta_2 = dezena_conta_1 % 10
print('O dígito das dezenas é {}'.format(int(dezena_conta_2)))
