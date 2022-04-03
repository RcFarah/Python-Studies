# Desafio #024

# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite a cidade em que você nasceu: ')).strip().title()
print('Sua cidade começa com a palavra Santo: {}'.format(cidade[:6] == 'Santo '))
