# Desafio #022

nome = str(input('Digite seu nome: ')).strip().title()
nome_maiu = nome.upper()
nome_minu = nome.lower()
letras_nome_todo = len(nome) - nome.count(' ')
nome_separado = nome.split()
print('Seu nome com todas as letras maiúsculas fica: {}\n'
      'Seu nome com todas as letras minúsculas fica: {}\n'
      'Seu nome tem ao todo {} letras.\n'
      'Seu primeiro nome tem {} letras.'.format(nome_maiu, nome_minu, letras_nome_todo, len(nome_separado[0])))
