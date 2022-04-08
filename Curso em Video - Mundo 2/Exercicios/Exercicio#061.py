# Exercicio #062

# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

primeiro_termo = int(input('Digite o valor do Primeiro Termo: '))
razao = int(input('Digite o valor da Razão: '))
termo = primeiro_termo
contador = 1


while contador <= 10:
    print(termo, '-> ', end='')
    termo += razao
    contador += 1
print('FIM')
