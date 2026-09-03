def rank_alunos(dic):
    rank = []
    for nome, lista_notas in dic.items():
        soma = 0
        size = 0
        # print(lista_notas)
        for nota in lista_notas:
            soma += nota
            size += 1
        media = soma/size
        tupla = (nome, media)
        rank.append(tupla)

    c = 0
    top = []
    while c < 3:
        maior = 0
        nome_aluno = ""
        for t in rank:
            if t[1] > maior:
                maior = t[1]
                nome_aluno = t[0]
        tupla2 = (nome_aluno, maior)
        top.append(tupla2)

    return top

dicionario = {"Marco" : [3.0, 6.50, 7.85],
              "Dani" : [9.0, 8.5, 10.0],
              "John" : [3.5, 4.75, 5.15],
              "Pablo" : [6.0, 6.0, 6.0]
              }

print(rank_alunos(dicionario))


