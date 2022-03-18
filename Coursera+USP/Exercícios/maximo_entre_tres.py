def maximo(numero_1, numero_2, numero_3):
    if numero_1 > numero_2 > numero_3 or numero_1 > numero_3 > numero_2:
        return numero_1
    elif numero_2 > numero_1 > numero_3 or numero_2 > numero_3 > numero_1:
        return numero_2
    elif numero_3 > numero_1 > numero_2 or numero_3 > numero_2 > numero_1:
        return numero_3
    else:
        return numero_1
