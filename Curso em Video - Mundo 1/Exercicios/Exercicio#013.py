# Desafio #013

salario_inicial = float(input('Qual o salário atual do funcionário? '))
porcentagem_aumento = int(input('Qual a porcentagem do aumento? '))
calculo_aumento = salario_inicial * (porcentagem_aumento / 100)
salario_final = salario_inicial + calculo_aumento
print('O funcionário terá um aumento de R${:.2f} em seu salário, que incialmente era de R${:.2f}, e passará a ter '
      'um salário de R${:.2f}'.format(calculo_aumento, salario_inicial, salario_final))
