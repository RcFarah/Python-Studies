# Exercicio #051

# Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma P.A. No final, mostre os 10 primeiros termos
# dessa progressão.

primeiro_termo = int(input('Digite o valor do Primeiro Termo: '))
razao = int(input('Digite o valor da Razão: '))
enesimo = primeiro_termo + (10 - 1) * razao

for progressao in range(primeiro_termo, enesimo + razao, razao):
    print(progressao)
