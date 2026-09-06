def rank_alunos(dic):
    lista_alunos = []
    lista_com_notas = []

    for aluno, lista_notas in dic.items():
        soma = 0
        for nota in lista_notas:
            soma += nota
        if len(lista_notas) != 0:
            media = round(soma/len(lista_notas), 2)
            tupla = (aluno, media)
        else:
            media = 0.00
            tupla = (aluno, media, "Sem nota")
        lista_alunos.append(tupla)

    # print(lista_alunos)
    lista_alunos = sorted(lista_alunos, key=lambda item: (-item[1], item[0]))
    # print(lista_alunos)

    for aluno in lista_alunos:
        if len(aluno) == 3:
            pass
        else:
            lista_com_notas.append(aluno)
    # print(lista_alunos)
    # print(lista_com_notas)

    if len(lista_com_notas) == 1:
        return [lista_com_notas[0]]
    elif len(lista_com_notas) == 2:
        return [lista_com_notas[0], lista_com_notas[1]]
    elif len(lista_com_notas) > 2:
        return [lista_com_notas[0], lista_com_notas[1], lista_com_notas[2]]
    else:
        return "Não existem alunos com notas"

dicionario = {"Marco" : [0.0],
              "Dani" : [9.0, 8.5, 10.0],
              "John" : [3.5, 4.75, 5.15],
              "Pablo" : [6.0, 6.0, 6.0],
              "Gordon": [6.0, 6.0, 6.0],
              "Jim": [],
              "DeMar": [0.0, 0.0]
              }

print(rank_alunos(dicionario))

