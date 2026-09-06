def produz_numeros(limite):
    soma = 1
    atual = 1
    yield 1

    while soma < limite:
        yield soma
        if soma == 1:
            soma = soma + atual
        else:
            soma = soma + atual
            atual = soma - atual

def main(limite):
    gerador = produz_numeros(limite)
    soma = 0
    for numero in gerador:
        print(numero)
        if numero % 2 == 0:
            soma += numero
    return soma

print(f"Soma dos pares de Fibonacci: {main(200)}")

# print(produz_numeros(10))

# gerador = produz_numeros(10)

# valor1 = next(gerador)
# print(valor1)
# valor2 = next(gerador)
# print(valor2)
# valor3 = next(gerador)
# print(valor3)

# for n in gerador:
#     print(n)

# feito em cerca de 19 min

