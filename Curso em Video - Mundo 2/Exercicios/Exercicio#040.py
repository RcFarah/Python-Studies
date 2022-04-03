# Exercicio #039

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

data = date

nascimento = int(input('Digite o ano do seu nascimento: '))

idade = date.today().year - nascimento
alistamento = nascimento + 18

if idade > 18:
    print('Já passou do tempo do seu alistamento militar!\n'
          'O seu alistamento foi em {}'.format(alistamento))
elif idade == 18:
    print('Já é hora de fazer o seu alistamento militar!\n'
          'O seu alistamento deverá ser feito IMEDIATAMENTE!')
elif idade < 18:
    print('Você ainda não precisa se alistar no serviço militar!\n'
          'Seu alistamento será em {}'.format(alistamento))
