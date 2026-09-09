def ordena(pessoas):
    # print(max(pessoas, key=lambda x : (x[1], -x[2])))
    nome, pontuacao, idade = max(pessoas, key=lambda x : (x[1], -x[2]))
    print(f"{nome} - {pontuacao} - {idade}")

pessoas = [
    ("Ana", 90, 22),
    ("Bruno", 95, 25),
    ("Carla", 95, 21),
    ("Diego", 88, 20)
]

ordena(pessoas)

#feito em 3min43s