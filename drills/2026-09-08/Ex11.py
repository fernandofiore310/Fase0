from collections import Counter


def conta_frutas(frutas):
    # dic = {}
    conta = Counter(frutas)

    # for fruta in frutas:
    #     dic[fruta] = conta[fruta]

    return dict(conta)

frutas = [
    "maçã",
    "banana",
    "maçã",
    "laranja",
    "banana",
    "maçã"
]

print(conta_frutas(frutas))

#feito em 5min