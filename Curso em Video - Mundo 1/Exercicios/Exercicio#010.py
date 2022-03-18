# Desafio #010

valorR = float(input('Qual o valor que você deseja converter? R$'))
dolar = valorR / 5.67
euro = valorR / 6.78
bitcoin = valorR / 274678.61
libraE = valorR / 7.88
iene = valorR / 0.053
litecoin = valorR / 1027.40
sel_moeda = str(input('Para qual moeda você deseja converter?')).strip().title()
if sel_moeda[0] == 'D':
    print('O valor que você pode comprar em Dólar com R${}, é de: ${:.2}'.format(valorR, dolar))
elif sel_moeda[0] == 'E':
    print('O valor que você pode comprar em Euro com R${}, é de: €{:.2}'.format(valorR, euro))
elif sel_moeda[0] == 'B':
    print('O valor que você pode comprar em Bitcoin com R${}, é de: BTC{:.2}'.format(valorR, bitcoin))
elif sel_moeda[0:3] == 'Lib':
    print('O valor que você pode comprar em Libra com R${}, é de: £{:.2}'.format(valorR, libraE))
elif sel_moeda[0] == 'I':
    print('O valor que você pode comprar em Ienem com R${}, é de: ¥{}'.format(valorR, iene))
elif sel_moeda[0:3] == 'Lit':
    print('O valor que você pode comprar em Litecoin com R${}, é de: LTC{:.2}'.format(valorR, litecoin))
else:
    print('Ops... Parece que você selecionou alguma opção errada, revise sua resposta!')
