# Desafio #023

# Opção 1
numero = int(input('Digite um número de 0 à 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o número {}, conclui-se que:\n'
      'Sua unidade é: {}\n'
      'Sua dezena é: {}\n'
      'Sua centena é: {}\n'
      'Seu milhar é: {}'.format(numero, unidade, dezena, centena, milhar))

# Opção 2
num = int(input('Digite um número de 0 à 9999: '))
if num < 10:
    n = str(num)
    print('Sua unidade é: {}'.format(n))
elif 10 < num < 100:
    n = str(num)
    print('Sua unidade é: {}\n'
          'Sua dezena é: {}'.format(n[1], n[0]))
elif 10 and 100 < num < 1000:
    n = str(num)
    print('Sua unidade é: {}\n'
          'Sua dezena é: {}\n'
          'Sua centena é: {}'.format(n[2], n[1], n[0]))
elif 10 and 100 and 1000 < num < 10000:
    n = str(num)
    print('Sua unidade é: {}\n'
          'Sua dezena é: {}\n'
          'Sua centena é: {}\n'
          'Seu milhar é: {}'.format(n[3], n[2], n[1], n[0]))
else:
    print('O número que você digitou não está dentre os limites estabelecidos, por favor, tente novamente.')

