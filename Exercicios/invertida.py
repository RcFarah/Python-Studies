seq = []
while True:
    numero = int(input())
    if (numero != 0):
        seq.append(numero)
    else:
        break

for i in seq[::-1]:
    print (i)
