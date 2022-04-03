# Exercicio #055

# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista_pesos = [] # Lista vazia

for peso in range(1, 7):
    peso_pessoa = float(input('Digite o peso da {}° pessoa: '.format(peso)))
    lista_pesos.append(peso_pessoa) # Adiciona o peso da pessoa
    lista_pesos.sort() # Ordena em ordem crescente

print('{} é o menor peso.\n'
      '{} é o maior peso.'.format(lista_pesos[0], lista_pesos[-1]))
