def list_normalizer(lista_nomes):
    lista_min = []
    lista_normalizada = []
    preposicoes = ["de", "da", "dos"]

    for nome in lista_nomes:
        lista_min.append(nome.lower())

    for nome_e_sobrenome in lista_min:

        if "," in nome_e_sobrenome:
            nome_e_sobrenome = nome_e_sobrenome.split()
            nome_e_sobrenome = f"{nome_e_sobrenome[1] + " " + nome_e_sobrenome[0]}"
            nome_e_sobrenome = nome_e_sobrenome.replace(",", "")
            # print(nome_e_sobrenome)
            l = nome_e_sobrenome.split()
            lista_correta = []
            for nome in l:
                # print(nome[0])
                if nome not in preposicoes:
                    nome = nome.replace(nome[0], nome[0].upper()) #string sao imutaveis, eh necessario atribuir um valor a ela
                # print(nome)
                lista_correta.append(nome)
            # print(lista_correta)
            nome_correto = " ".join(lista_correta)
            if nome_correto not in lista_normalizada:
                lista_normalizada.append(nome_correto)

        else:
            nome_e_sobrenome = nome_e_sobrenome.split()
            lista_correta = []
            # print(nome_e_sobrenome)
            for nome in nome_e_sobrenome:
                if nome not in preposicoes:
                    nome = nome.replace(nome[0], nome[0].upper())
                lista_correta.append(nome)
            # print(lista_correta)
            nome_correto = " ".join(lista_correta)
            # print(nome_correto)
            if nome_correto not in lista_normalizada:
                lista_normalizada.append(nome_correto)

    return lista_normalizada


lista_nomes = ["mARCO tULIO", "tulio, mArco", " cleber dos anjos ", "BeRnARdo mayrinck"]
lista_final = list_normalizer(lista_nomes=lista_nomes)
print(lista_final)