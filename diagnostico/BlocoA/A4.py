def conta_frequencia(texto, n, stopwords):
    dicionario_palavras = {}
    palavras_frequentes = []

    texto = texto.lower()
    lista_texto = texto.split()
    for palavra in lista_texto:
        if palavra not in dicionario_palavras:
            dicionario_palavras[palavra] = 1
        else:
            dicionario_palavras[palavra] += 1
    # print(dicionario_palavras)
    print(sorted(dicionario_palavras.items()))
    lista_freq = sorted(dicionario_palavras.items())

    i = 0
    while i < n:
        maior = 0
        p = ""
        index = 0
        c = 0
        for tupla in lista_freq:
            if tupla[1] > maior:
                maior = tupla[1]
                p = tupla[0]
                index = c
            c += 1
        palavras_frequentes.append(p)
        del lista_freq[index]
        i+=1

    print(palavras_frequentes)
    
texto = "Meu dia começou assim: mandei quatro ovos com manteiga, com duas fatias de bacon, um quarto de abacate, com um café preto para acompanhar e um suco de laranja natural."
print(conta_frequencia(texto, 4, []))