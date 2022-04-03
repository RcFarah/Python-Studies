# Desafio #012

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto_preco = float(input('Qual o preço do produto? '))
desconto = int(input('Qual a % de desconto que deseja aplicar? '))
calculo_desconto = produto_preco * (desconto / 100)
preco_com_desconto = produto_preco - calculo_desconto
print('O produto que custava R${}, com o desconto de {}%, passou a custar R${}.'.format(produto_preco, desconto,
                                                                                        preco_com_desconto))
