# Desafio #035

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

segmento_a = float(input('Coloque o valor de um lado: '))
segmento_b = float(input('Coloque o valor de outro lado: '))
segmento_c = float(input('Coloque o valor de outro lado: '))

if segmento_a < segmento_b + segmento_c and segmento_b < segmento_a + segmento_c and segmento_c < segmento_a + segmento_b:
    print('Os lados {}, {} e {} podem formar triângulo.'.format(segmento_a, segmento_b, segmento_c))
else:
    print('Os lados {}, {} e {} não podem formar triângulo.'.format(segmento_a, segmento_b, segmento_c))
