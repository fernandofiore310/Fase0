def mapeia(lista):
    lista_categorias = []
    for dic in lista:
        if dic["categoria"] not in lista_categorias:
            lista_categorias.append(dic["categoria"])

    dicionario = {}
    for categoria in lista_categorias:
        total = 0
        quantidade = 0
        maior_valor = 0
        for dic in lista:
            if dic["categoria"] == categoria:
                total += dic["valor"]
                quantidade += 1
                maior_valor = max(maior_valor, dic["valor"])
        tupla = (total, quantidade, maior_valor)
    