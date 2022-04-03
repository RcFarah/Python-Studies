# Desafio  #015

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

import random
from time import sleep

nome_cliente = str(input('Qual o nome do cliente? ')).strip().title()
cpf_cliente = str(input('Qual o CPF do cliente? ')).strip()
print('CONSULTANDO EM NOSSO BANCO DE DADOS...')
sleep(1.5)
print('CONSULTA CONCLUÍDA.')
print('--' * 10)
print('CARRO ALUGADO: {}\n'
      'NOME DO CLIENTE: {}\n'
      'CPF DO CLIENTE: {}'
      .format(random.choice(['Kia Cerato', 'Ford Ka', 'HB20', 'Audi A3', 'Kia Soul', 'Crossfox']),
              nome_cliente, cpf_cliente))
preco_diaria = 60
preco_km = 0.15
dias_alugado = int(input('Quantos dias o carro ficou alugado? '))
km_percorrido = float(input('Quantos KM''s foram percorridos? '))
diaria_total = dias_alugado * preco_diaria
km_preco_total = km_percorrido * preco_km
conta_total = km_preco_total + diaria_total
print('--' * 10)
print('O valor da diária é de: R${:.2f}\n'
      'O valor do KM rodado é de: R${:.2f}'.format(preco_diaria, preco_km))
print('--' * 10)
print('O valor a ser pago pelas diárias é de: R${:.2f}\n'
      'O valor a ser pago pelos KM''s rodados é de: R${:.2f}\n'
      'O valor total a ser pago é de: R${:.2f}'.format(diaria_total, km_preco_total, conta_total))
