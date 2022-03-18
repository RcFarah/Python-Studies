# Exercicio #043

altura = int(input('Digite a sua alutra (em cm): '))
peso = int(input('Digite o seu peso (em KG): '))
altura_metro = altura / 100
calculo_imc = peso / (altura_metro ** 2)

if calculo_imc < 18.5:
    print('Abaixo do Peso.')
elif 18.5 < calculo_imc < 25:
    print('Peso Ideal!')
elif 25 <= calculo_imc < 30:
    print('Sobrepeso.')
elif 30 <= calculo_imc <= 40:
    print('Obesidade.')
elif calculo_imc > 40:
    print('Obesidade Mórbida.')
