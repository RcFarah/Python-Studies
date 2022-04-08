# Exercicio #062

# # Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o valor do Primeiro Termo: '))
razao = int(input('Digite o valor da Razão: '))
termo = primeiro_termo
contador = 1
mais_termo = 10
total = 0

while mais_termo != 0:
    total = total + mais_termo
    while contador <= total:
        print(termo, '-> ', end='')
        termo += razao
        contador += 1
    mais_termo = int(input('Deseja mostrar mais quantos termos (0 para finalizar): '))
print('Progressão Aritmética finalizada com {} termos.'.format(total))
print('FIM')
