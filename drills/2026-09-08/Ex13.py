def dobra_numeros(numeros):
    for n in numeros:
        n = n*2

    print(numeros)

numeros = [1, 2, 3, 4]
dobra_numeros(numeros)

# feito em 2min

# Quando fazemos:
# for n in numeros:
#     n = n * 2
#
# a variável n recebe, a cada iteração, uma referência ao valor atual da lista.
#
# Como inteiros são imutáveis, a expressão n * 2 cria um novo inteiro.
# Depois disso, n passa a referenciar esse novo valor.
#
# Porém, isso NÃO altera a posição correspondente dentro da lista.
# A lista continua contendo os valores originais.
#
# Ou seja:
# n = n * 2
# altera apenas a variável n
#
# Já:
# numeros[indice] = n * 2
# altera de fato o elemento armazenado naquela posição da lista.
#
# Por isso, se quisermos modificar a própria lista durante o loop,
# podemos usar enumerate para obter índice e valor:
#
# for i, n in enumerate(numeros):
#     numeros[i] = n * 2
#
# Outra opção seria usar uma list comprehension,
# mas nesse caso normalmente criamos uma nova lista.