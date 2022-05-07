# Exercicio #057

#  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
#  peça a digitação novamente até ter um valor correto.

from datetime import date
from time import sleep

data_atual = date.today()
data_atual_br = data_atual.strftime('%d/%m/%Y')
idade = 0
sexo = ''
nome_plano = ''
tipo_alergia = ''
contatos = []

print('-' * 10, 'FICHA MÉDICA', '-' * 10, end='\n \n')

nome = str(input('Digite o nome completo do paciente: ')).strip().title()

# receber e transformar a data de nascimento para o padrão BR
dia_nasc = int(input('Dia do nascimento: '))
mes_nasc = int(input('Mês do nascimento: '))
ano_nasc = int(input('Ano do nascimento: '))
data_nasc = date(ano_nasc, mes_nasc, dia_nasc)
data_nasc_texto = data_nasc.strftime('%d/%m/%Y')

# descobrir idade
if mes_nasc > date.today().month:
    idade = (date.today().year - ano_nasc) - 1
elif mes_nasc == date.today().month:
    if dia_nasc <= date.today().day:
        idade = date.today().year - ano_nasc
    elif dia_nasc > date.today().day:
        idade = (date.today().year - ano_nasc) - 1

# receber os tipos de contato
telefone_contato = str(input('Digite o número de telefone para contato do paciente: +55 21 ')).strip()
email_contato = str(input('Digite o email de contato do paciente: '))
contatos = [telefone_contato, email_contato]

# desafio do exercicio incrementado
sexo_opcao = str(input('Escolha uma opção para o sexo do paciente:\n'
                       '[M] Masculino\n'
                       '[F] Feminino\n'
                       '[O] Outros\n')).upper().strip()
if sexo_opcao == 'M':
    sexo = 'Masculino'
elif sexo_opcao == 'F':
    sexo = 'Feminino'
elif sexo_opcao == 'O':
    sexo = 'Outros'

while sexo_opcao not in ['M', 'F', 'O']: # ou while sexo_opcao not in 'MFO':
    print('Opção inválida, por favor revise e tente novamente.')
    sexo_opcao = str(input('Escolha uma opção para o sexo do paciente:\n'
                           '[M] Masculino\n'
                           '[F] Feminino\n'
                           '[O] Outros\n')).title().strip()
    if sexo_opcao == 'M':
        sexo = 'Masculino'
    elif sexo_opcao == 'F':
        sexo = 'Feminino'
    elif sexo_opcao == 'O':
        sexo = 'Outros'

# informações extras
plano_saude = str(input('O paciente possui Plano de Saúde? (Sim/Não): ')).strip().upper()
if plano_saude == 'SIM':
    nome_plano = str(input('Qual? ')).strip().upper()
else:
    nome_plano = '-'
    plano_saude = 'NÃO'

# informações necessárias
tipo_sanguineo = str(input('Digite o tipo sanguíneo do paciente: '))
fumante = str(input('O paciente é fumante? (Sim/Não): ')).strip().upper()
alcoolatra = str(input('O paciente é alcoólatra? (Sim/Não): ')).strip().upper()
drogas = str(input('O paciente é usuário de drogas? (Sim/Não): ')).strip().upper()
alergia = str(input('O paciente possui alguma alergia? (Sim/Não): ')).strip().upper()
if alergia == 'SIM':
    tipo_alergia = str(input('Alergia a que: ')).strip().upper()
else:
    tipo_alergia = '-'
    alergia = 'NÃO'

# Como sai na impressão
imprimir = str(input('Deseja imprimir a ficha? (Sim/Não): ')).strip().upper()
if imprimir == 'SIM':
    print('AGUARDE ENQUANTO IMPRIMIMOS.\n \n \n ')
    sleep(3)
    print('-' * 10, 'FICHA MÉDICA', '-' * 10, end='\n \n')
    print('Nome: {}\n'
          'Data de Nascimento: {}     Idade: {}\n'
          'Sexo: {}       Tipo Sanguíneo: {}\n'
          'Plano de Saúde? {}       Qual: {}\n'
          'Fumante: {}       Alcoólatra: {}\n'
          'Usuário de Drogas: {}\n'
          'Alérgico? {}       Alergias: {}\n \n'.format(nome, data_nasc_texto, idade, sexo, tipo_sanguineo, plano_saude,
                                                        nome_plano, fumante, alcoolatra, drogas, alergia, tipo_alergia),
          '_' * 40, end='\n \n')
    print('Contatos:\nEmail: {}     Telefone: {}'.format(contatos[1], contatos[0]))
    print('\n' * 4,
          '-' * 10, '{}'.format(data_atual_br), '-' * 10)
    print('\n \n \n IMPRESSÃO FINALIZADA')
else:
    print('Cadastro Finalizado')
