# Desafio #005

num1 = float(input('Digite um número: '))
ant = num1 - 1
suc = num1 + 1
print('Analisando o número {}, conclui-se que seu \033[31mANTECESSOR\033[m é {} e seu \033[31mSUCESSOR\033[m é {}.'
      .format(num1, ant, suc))
