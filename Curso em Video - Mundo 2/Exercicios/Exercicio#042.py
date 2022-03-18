# Exercicio #042

seg_a = int(input('Digite o valor do segmento a: '))
seg_b = int(input('Digite o valor do segmento b: '))
seg_c = int(input('Digite o valor do segmento c: '))

if (seg_b - seg_c) < seg_a < seg_b + seg_c and (seg_a - seg_c) < seg_b < seg_a + seg_c and (seg_a - seg_b) < seg_c < \
        seg_a + seg_b:
    print('Esses segmentos podem formar um triângulo!')
    if seg_a == seg_b == seg_c:
        print('Esse é um triangulo EQUILÁTERO!')
    elif seg_a != seg_b != seg_c:
        print('Esse é um triângulo ESCALENO!')
    else:
        print('Esse é um triângulo ISÓSCELES!')
else:
    print('Esses segmentos não podem formar um triângulo...')
