def ordena(alunos):
    return sorted(alunos, key=lambda x : (-x[1], x[0]))

alunos = [
    ("Carlos", 8.0),
    ("Ana", 9.0),
    ("Bruno", 8.0),
    ("Daniela", 9.0)
]

print(ordena(alunos))

# feito em 3min5s