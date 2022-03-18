numero = input("Informe um número: ")
primo = False

if numero.isdigit():

    numero = int(numero)

    if numero > 1:
        if numero == 2:
            primo = True
        else:
            i = 2
            while i <= numero and not primo:
                if (not numero % 2 == 0
                    and numero % i == 0 and i == numero):
                    primo = True
                i += 1

    if primo:
        print("primo")
    else:
        print("não primo")
