# Desafio #011

larg_parede = float(input('Digite a largura da parede da qual você deseja pintar (em Metros): '))
alt_parede = float(input('Digite a altura da parede da qual você deseja pintar (em Metros): '))
area = larg_parede * alt_parede
print('Sua parede tem a dimensão de {}x{} e a área da sua parede é de {}m²'.format(larg_parede, alt_parede, area))
tinta = area / 2
print('Você precisará de {:.2}L de tinta para pintar sua parede!'.format(tinta))
