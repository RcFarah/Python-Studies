numero = int(input("Digite um numero: "))
anterior = numero % 10
numero = numero // 10
adj_iguais = False
pos = 0
while numero > 0 and not adj_iguais:
    atual = numero % 10
    if atual == anterior:
        adj_iguais = True
    else:
        pos += 1
    anterior = atual
    numero = numero // 10

if adj_iguais:
    print("sim")
else:
    print("não")
