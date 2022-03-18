print("Cálculo do fatorial de um número\n")
n = int(input("Digite um número inteiro não-negativo: "))
i = 1
n_fatorial = 1
while i <= n:
    n_fatorial = n_fatorial * i
    i = i + 1
print("{}".format(n_fatorial))
