def exponencial(numero_base, potencia):
    result = 1
    for index in range(potencia):
        result = result * numero_base
        return result
    print(exponencial(3, 4))