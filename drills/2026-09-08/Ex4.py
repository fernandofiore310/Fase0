def ordena(pessoas):
    return sorted(pessoas, key=lambda x : x[1])

pessoas = [
    ("Carlos", 31),
    ("Ana", 22),
    ("Bruno", 47),
    ("Daniela", 19)
]

print(ordena(pessoas))

# feito em 2 min