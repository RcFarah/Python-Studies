# Desafio #014

unid_temp = str(input('De que unidade de temperatura que deseja fazer a conversão? ')).strip().title()
temperatura = float(input('Qual a temperatura incial? (SOMENTE NÚMERO) '))
unid_converter = str(input('Para qual unidade que deseja fazer a conversão? ')).strip().title()
if unid_temp[0] == 'C':
    if unid_converter[0] == 'F':
        calculo = (temperatura * 1.8) + 32
        print('{}ºC equivale a {}ºF'.format(temperatura, calculo))
    elif unid_converter[0] == 'K':
        calculo = temperatura + 273.15
        print('{}ºC equivale a {}K'.format(temperatura, calculo))
    else:
        print('Você digitou uma unidade inexistente, por favor, revise e tente novamente!')
elif unid_temp[0] == 'F':
    if unid_converter[0] == 'C':
        calculo = (temperatura - 32) * 1.8
        print('{}ºF equivale a {}ºC'.format(temperatura, calculo))
    elif unid_converter[0] == 'K':
        calculo = ((temperatura - 32) / 1.8) + 273.15
        print('{}° equivale a {}K'.format(temperatura, calculo))
    else:
        print('Você digitou uma unidade inexistente, por favor, revise e tente novamente!')
elif unid_temp[0] == 'K':
    if unid_converter[0] == 'C':
        calculo = temperatura - 273.15
        print('{}K equivale a {}°C'.format(temperatura, calculo))
    elif unid_converter[0] == 'F':
        calculo = ((temperatura - 273.15) * 1.8) + 32
        print('{}K equivale a {}°F'.format(temperatura, calculo))
    else:
        print('Você digitou uma unidade inexistente, por favor, revise e tente novamente!')
else:
    print('Alguma coisa que você digitou está incorreta, revise suas respostas e tente novamente!')
