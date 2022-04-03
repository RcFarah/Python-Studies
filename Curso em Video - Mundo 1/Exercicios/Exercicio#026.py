# Desafio #026

# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).strip().lower()
print('Na frase{}\n'
      'A letra "A" aparece {} vezes na frase.\n'
      'A primeira letra "A" apareceu na {} posição.\n'
      'A última letra "A" apareceu na {} posição.'.format(frase, frase.count('a'), frase.find('a') + 1,
                                                          frase.rfind('a') + 1))
