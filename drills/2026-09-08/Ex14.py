def remove_negativos(numeros):
    for n in numeros:
        if n < 0:
            numeros.remove(n)

    print(numeros)

numeros = [3, -1, 5, -2, 0, 8, -4]
remove_negativos(numeros)

# feito em 2min15s

# Ele pula 5 e 0.
#
# O que acontece é:
# - começa em 3
# - vai para -1 e remove esse valor
# - a lista vira [3, 5, -2, 0, 8, -4]
# - o iterador avança para o próximo índice, então cai em -2 e pula o 5
# - remove -2
# - a lista vira [3, 5, 0, 8, -4]
# - avança de novo e cai em 8, pulando o 0
# - depois chega em -4
#
# Por isso o resultado final saiu certo:
# os elementos que foram pulados (5 e 0) eram positivos,
# então não precisavam ser removidos.
#
# Se houvesse dois negativos consecutivos, o bug apareceria,
# porque um dos negativos poderia ser pulado.