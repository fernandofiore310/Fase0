def conta_frequencia(texto, n, stopwords):
    texto = texto.lower()
    pontuacao = [".", ",", "?", "!"]
    lista_palavras = []

    for p in texto:
        palavra = ""
        for c in p:
            if c not in pontuacao:
                palavra += c
        if palavra not in stopwords:
            lista_palavras.append(palavra)

    

print(conta_frequencia("Oi, tudo bem?", 3))