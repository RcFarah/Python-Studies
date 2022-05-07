# Exercicio #070

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Iniciando variaveis iniciais
total_produtos = produtos_mais_de_mil = total_a_pagar = 0
preco_produto_mais_barato = 9999999999999999
nome_produto_mais_barato = ''


print('-' * 25)
print('PROGRAMA INICIADO.')
print('-' * 25)

while True:

    # Cadastro dos produtos
    produto = str(input('INSIRA O NOME DO PRODUTO: ')).strip().title()
    preco_produto = float(input('INSIRA O PREÇO DO PRODUTO: R$'))

    # Parte do desafio
    total_produtos += 1
    total_a_pagar += preco_produto
    if preco_produto > 1000:
        produtos_mais_de_mil += 1


    if preco_produto < preco_produto_mais_barato:
        nome_produto_mais_barato = produto
        preco_produto_mais_barato = preco_produto

    # Criação de condição de parada

    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? (S/N): ')).upper().strip()[0]
    if continuar == 'N':
        print('-' * 25)
        print('EFETUANDO CÁLCULOS.')
        print('-' * 25)
        break


    print('-' * 25, end='\n')

# Print do pedido do programa
print('\nSua compra com o total de {} produtos foi efetuada.\n'
      'PREÇO TOTAL: R${}\n'
      'Produtos que custam mais de R$1000,00: {}\n'
      'Produto mais barato: {}, que custa R${}'.format(total_produtos, total_a_pagar, produtos_mais_de_mil,
                                                      nome_produto_mais_barato, preco_produto_mais_barato))
