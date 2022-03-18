# Exercicio #044

valor_original = float(input('Digite o valor do produto: R$'))
forma_pagamento = int(input('Qual a forma de pagamento?\n'
                            '(1) para Dinheiro\n'
                            '(2) para Á vista no Cartão\n'
                            '(3) para Até 2x no Cartão\n'
                            '(4) para 3x ou mais no Cartão\n'
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
