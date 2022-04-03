# Desafio #034

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario_base = float(input('Qual o salário atual do funcionário? '))
if salario_base > 1250:
    salario_acrescimo = salario_base * (10 / 100)
    salario_novo = salario_base + salario_acrescimo
    print('O novo salário será de: R${:.2f}'.format(salario_novo))
elif salario_base <= 1250:
    salario_acrescimo = salario_base * (15 / 100)
    salario_novo = salario_base + salario_acrescimo
    print('O novo salário será de: R${:.2f}'.format(salario_novo))
