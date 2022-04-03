# Desafio #017

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.

print('Nesse programa iremos te dizer qual deverá ser o tamanho da hipotenusa de um Triângulo, para que ele se feche.')
print('--' * 10)
cateto_oposto = float(input('Digite o tamanho do Cateto Oposto: '))
cateto_adjacente = float(input('Digite o tamanho do Cateto Adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1 / 2)
print('O valor da hipotenusa, para um triângulo com tais medidas, é de: {:.2f}'.format(hipotenusa))
