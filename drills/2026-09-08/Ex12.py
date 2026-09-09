from collections import defaultdict


def agrupa(lista):
    dic = defaultdict(list)
    # print(dic)

    for item in lista:
        dic[item[0]].append(item[1])

    return dict(dic)

itens = [
    ("fruta", "maçã"),
    ("bebida", "água"),
    ("fruta", "laranja"),
    ("bebida", "suco"),
    ("fruta", "uva")
]

print(agrupa(itens))

#feito em 5min30s