def pares(lista):
    return [n**2 for n in lista if n % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 10]
print(pares(numeros))

# feito em 3min2s