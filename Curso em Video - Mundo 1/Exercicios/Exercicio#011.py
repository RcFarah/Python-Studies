# Desafio #011

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg_parede = float(input('Digite a largura da parede da qual você deseja pintar (em Metros): '))
alt_parede = float(input('Digite a altura da parede da qual você deseja pintar (em Metros): '))
area = larg_parede * alt_parede
print('Sua parede tem a dimensão de {}x{} e a área da sua parede é de {}m²'.format(larg_parede, alt_parede, area))
tinta = area / 2
print('Você precisará de {:.2}L de tinta para pintar sua parede!'.format(tinta))
