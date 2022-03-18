# Exercicio #039

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
