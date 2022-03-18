# Desafio #026

frase = str(input('Escreva uma frase: ')).strip().lower()
print('Na frase{}\n'
      'A letra "A" aparece {} vezes na frase.\n'
      'A primeira letra "A" apareceu na {} posição.\n'
      'A última letra "A" apareceu na {} posição.'.format(frase, frase.count('a'), frase.find('a') + 1,
                                                          frase.rfind('a') + 1))
