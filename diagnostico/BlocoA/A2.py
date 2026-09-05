def rank_alunos(dic):
    lista_alunos = []

    for aluno, lista_notas in dic.items():
        soma = 0
        for nota in lista_notas:
            soma += nota
        if len(lista_notas) != 0:
            media = round(soma/len(lista_notas), 2)
        else:
            media = 0.00
        tupla = (aluno, media)
        lista_alunos.append(tupla)

    # print(lista_alunos)
    lista_alunos = sorted(lista_alunos, key=lambda item: (-item[1], item[0]))
    print(lista_alunos)

    for aluno in lista_alunos:
        if aluno[1] == 0.0:
            lista_alunos.remove(aluno)
    print(lista_alunos)

    return [lista_alunos[0], lista_alunos[1], lista_alunos[2]]

dicionario = {"Marco" : [3.0, 6.50, 7.85],
              "Dani" : [9.0, 8.5, 10.0],
              "John" : [3.5, 4.75, 5.15],
              "Pablo" : [6.0, 6.0, 6.0],
              "Gordon": [6.0, 6.0, 6.0],
              "Jim": []
              }

print(rank_alunos(dicionario))


