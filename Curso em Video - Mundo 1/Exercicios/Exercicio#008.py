# Desafio #008

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Conversor de Medidas de Metro para: Decametro, Hectometro, Quilometro, Decímetro, Centímento e Milímetro.')
medida_metros = float(input('Digite uma medida em metros: '))
medida_dam = medida_metros * 10
medida_hm = medida_metros * 100
medida_km = medida_metros * 1000
medida_dm = medida_metros / 10
medida_cm = medida_metros / 100
medida_mm = medida_metros / 1000
print('A medida \033[31m{} m\033[m corresponde a:\n'
      'Milímetro: \033[31m{} mm\033[m\n'
      'Centímetro: \033[31m{} cm\033[m\n'
      'Decímetro: \033[31m{} dm\033[m\n'
      'Decametro: \033[31m{} dam\033[m\n'
      'Hectometro: \033[31m{} hm\033[m\n'
      'Quilometro: \033[31m{} km\033[m\n'
      'Espero que tenha te ajudado!'.format(medida_metros, medida_mm, medida_cm, medida_dm, medida_dam, medida_hm,
                                            medida_km))
