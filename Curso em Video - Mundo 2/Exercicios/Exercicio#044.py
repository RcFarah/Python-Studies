# Exercicio #044

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print('{:-^40}'.format(' LOJA DE AÇUDE '))  # O ^ serve para indicar que é para preencher o que se pede dentro de X
# caracteres

valor_original = float(input('\nDigite o valor do produto: R$'))
forma_pagamento = int(input('\nQual a forma de pagamento?\n'
                            '[1] para Dinheiro\n'
                            '[2] para Á vista no Cartão\n'
                            '[3] para Até 2x no Cartão\n'
                            '[4] para 3x ou mais no Cartão (Juros de 20%)\n'
                            'Digite: '))

if forma_pagamento == 1:
    desconto_dinheiro = valor_original * (10 / 100)
    valor_dinheiro = valor_original - desconto_dinheiro
    print('O valor total a ser pago é de: R${:.2f}\n'
          'Desconto total aplicado: R${:.2f}'.format(valor_dinheiro, desconto_dinheiro))

elif forma_pagamento == 2:
    desconto_cartao = valor_original * (5 / 100)
    valor_cartao_avista = valor_original - desconto_cartao
    print('O valor total a ser pago é de: R${:.2f}\n'
          'Desconto total aplicado: R${:.2f}'.format(valor_cartao_avista, desconto_cartao))

elif forma_pagamento == 3:
    print('O valor total a ser pago é de: R${:.2f}'.format(valor_original))

elif forma_pagamento == 4:
    acrescimo_cartao = valor_original * (20 / 100)
    valor_cartao_parcelado = valor_original + acrescimo_cartao
    print('O valor total a ser pago é de: R${:.2f}\n'
          'Valor dos Juros Aplicados: R${:.2f}'.format(valor_cartao_parcelado, acrescimo_cartao))

else:
    print('Forma de pagamento inválido, por favor, tente novamente!')
