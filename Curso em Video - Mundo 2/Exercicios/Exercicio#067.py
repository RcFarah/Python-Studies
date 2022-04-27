# Exercicio #067

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

tabuada = numero = resultado = 0

while True:
    print('__' * 23)
    numero = int(input('Digite o número que deseja descobrir a tabuada\n'
                       '(para sair, digite qualquer número negativo): '))
    if numero < 0:
        break
    for tabuada in range(0, 11):
        resultado = numero * tabuada
        print('{} x {} = {}'.format(numero, tabuada, resultado))
        tabuada += 1
