nome_Cliente = str(input('Nome do Cliente: '))
dia_vencimento_cartao = str(input('Digite o DIA de vencimento do cartão: '))
mes_vencimento_cartao = str(input('Digite o MÊS de vendcimento do cartão: '))
valor_fatura = str(input('Digite o VALOR da FATURA: R$'))
print('Olá, {}\nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.'
      .format(nome_Cliente, dia_vencimento_cartao, mes_vencimento_cartao, valor_fatura))
