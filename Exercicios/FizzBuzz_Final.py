def fizzbuzz(numero):
    divisao3 = numero % 3
    divisao5 = numero % 5
    divisao15 = numero % 15
    if divisao3 == 0 and divisao5 != 0:
        return 'Fizz'
    elif divisao3 != 0 and divisao5 == 0:
        return 'Buzz'
    elif divisao15 == 0:
        return 'FizzBuzz'
    else:
        return numero
