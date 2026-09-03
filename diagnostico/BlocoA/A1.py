def list_normalizer(lista_nomes):
    lista_normalizada = []
    for nome in lista_nomes:
        nome = nome.lower()
        nome_arrumado = ""
        for c in nome:
            if c == c[0] and c[0] != " ":
                nome_arrumado[0] = c[0].upper()
            elif c == c[0] and c[0] == " ":
                nome.remove(c[0])
        lista_normalizada.append(nome_arrumado)
        
    return lista_normalizada
            
