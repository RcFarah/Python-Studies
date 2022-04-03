# Desafio 036

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.

from time import sleep
from sys import exit

print('Olá, seja bem vindo ao Banco Rodrigun City Bank.')
cadtest = str(input('Qual opção deseja:\nCadastro\nTeste\n')).strip().lower()
if cadtest[0] == 'c':
    print('Para prosseguir com o cadastro, siga os passos a seguir!')
    nome = str(input('Digite seu nome completo: ')).strip().title()
    nascimento = str(input('Digite sua data de nascimento: ')).strip()
    nacionalidade = str(input('Digite o país em que você nasceu: ')).strip().title()
    cpf = str(input('Digite seu CPF: ')).strip()
    print('Verifique se seus dados estão corretos: Meu nome é {}, nascido em {}, no país {}, possuo o CPF {}'
          .format(nome, nascimento, nacionalidade, cpf))
    certo = str(input('Os dados estão corretos?\n (RESPONDA COM "SIM" OU "NÃO"!)\n')).strip().lower()
    if certo[0] == 'n':
        print('Preencha novamente todos os dados.')
        print('Para prosseguir com o cadastro, siga os passos a seguir!')
        nome = str(input('Digite seu nome completo: ')).strip().title()
        nascimento = str(input('Digite sua data de nascimento: ')).strip()
        nacionalidade = str(input('Digite o país em que você nasceu: ')).strip().title()
        cpf = str(input('Digite seu CPF: ')).strip()
        print('Verifique se seus dados estão corretos: Meu nome é {}, nascido em {}, no país {}, possuo o CPF {}'
              .format(nome, nascimento, nacionalidade, cpf))
    elif certo[0] == 's':
        print('Estamos armazenando os dados em nosso sistema, aguarde alguns instantes.')
        sleep(4)
        print('Olá, {}, para prosseguirmos com a liberação do empréstimo, precisamos de mais alguns dados!'.format(nome)
              )
        sal = float(input('Qual o seu salário mensal? R$'))
        valcasa = float(input('Qual o valor da casa? R$'))
        payanos = int(input('Em quantos anos deseja pagar a casa? '))
        certo2 = str(input('Verifique se os dados estão corretos, isso poderá alterar o resultado final da liberação:\n'
                           '(RESPONDA COM "SIM" OU "NÃO"!)\n')).strip().lower()
        if certo2[0] == 'n':
            print('Preencha novamente todos os dados.')
            print('Olá, {}, para prosseguirmos com a liberação do empréstimo, precisamos de mais alguns dados!'.format(
                nome))
            sal = float(input('\nQual o seu salário mensal? R$'))
            valcasa = float(input('Qual o valor da casa? R$'))
            payanos = int(input('Em quantos anos deseja pagar a casa? '))
            certo2 = str(
                input('Verifique se os dados estão corretos, isso poderá alterar o resultado final da liberação:\n'
                      '(RESPONDA COM "SIM" OU "NÃO"!)\n')).strip().lower()
        else:
            prestmensal = valcasa / (payanos * 12)
            print('O valor total da prestação mensal será de: R${}'.format(prestmensal))
            if prestmensal > sal / (30 / 100):
                print('Infelizmente a prestação mensal ultrapassa os 30% limite do seu salário,\n e com isso '
                      'não poderemos fazer a liberação do empréstimo...')
            else:
                print('Parabéns, você está apto(a) a conseguir a liberação do empréstimo!\n Para prosserguirmos com o '
                      'empréstimo, por favor, confirme novamente alguns dados.')
                cpf = input('Digite seu CPF:')
                nome_completo = str(input('Insira seu nome completo: ')).strip().title()
                agencia = int(input('Digite a sua agência bancária: '))
                confirm = input('Confirme se todos os dados estão corretos. (Responda somente com'
                                ' "SIM" ou "NÃO"): ').strip().title()
                if confirm[0] == "S":
                    print('Aguarde enquanto checamos os dados em nosso sistema.')
                    sleep(4)
                    print('Seu saldo estará disponível em no máximo 3 dias úteis, em sua conta.')
                    print('Encerrando o sistema em 5 segundos.')
                    sleep(5)
                    exit()

elif cadtest[0] == 't':
    sal = float(input('Qual o seu salário mensal? R$'))
    valcasa = float(input('Qual o valor da casa? R$'))
    payanos = int(input('Em quantos anos deseja pagar a casa? '))
    prestmensal = valcasa / (payanos * 12)
    print('O valor total da prestação mensal será de: R${}'.format(prestmensal))
    if prestmensal > sal / (30 / 100):
        print('Infelizmente a prestação mensal ultrapassa os 30% limite do seu salário,\n e com isso '
              'não poderemos fazer a liberação do empréstimo...')
    else:
        print('Parabéns, você está apto(a) a conseguir a liberação do empréstimo!')
else:
    print('Parece que você escolheu alguma opção inexistente... Tente novamente!')
