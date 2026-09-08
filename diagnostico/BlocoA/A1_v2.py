def normalizer(lista):
    lista_min = []
    nomes_arrumados = []
    preposicoes = ["de", "da", "dos"]

    for nome in lista:
        lista_min.append(nome.lower())

    for nome_completo in lista_min:
        if "," in nome_completo:
            nome_completo = nome_completo.replace(",", "")
            # print(nome_completo)
            nome_completo = nome_completo.split()
            nome_arrumado = nome_completo[1] + " " + nome_completo[0]
            nomes_arrumados.append(nome_arrumado)
        else:
            nome_completo = nome_completo.split()
            print(nome_completo)
            for nome in nome_completo:
                if nome not in preposicoes:
                    nome = nome[0].upper() + nome[1:]
            print(nome_completo)
            nome_arrumado = nome_completo[0] + " " + nome_completo[1]
            nomes_arrumados.append(nome_arrumado)

    # print(nomes_arrumados)

l = ["silva, marcos", "JOHN DoE", " hal jordan  ", "jordan, hal", "maria de souza"]
print(normalizer(l))