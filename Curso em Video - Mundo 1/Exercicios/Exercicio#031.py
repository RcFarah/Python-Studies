# Desafio #031

# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,
# 50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km_viagem = int(input('Qual a distância da viagem? (Favor botar distância em Km): '))
preco_viagem_curta = 0.5 * km_viagem
preco_viagem_longa = 0.45 * km_viagem
if km_viagem < 200:
    print('O preço a se pagar pela passagem dessa viagem é de: R${:.2f}'.format(preco_viagem_curta))
else:
    print('O preço a se pagar pela passagem dessa viagem é de: R${:.2f}'.format(preco_viagem_longa))
