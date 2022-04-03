# Exercicio #049

# Refaça o Exercicio#009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite o número que deseja saber a tabuada: '))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print('{} x {} = {}'.format(numero, multiplicador, resultado))


# OU

# numero = int(input('Digite o número que deseja saber a tabuada: '))
# for multiplicador in range(1, 11):
#   print('{} x {} = {}'.format(numero, multiplicador, numero * multiplicador)
