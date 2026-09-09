def ordena(lista):
    return sorted(lista, key=lambda x : (x[1], -x[2], x[0]))

produtos = [
    ("Mouse", "Acessórios", 120),
    ("Teclado", "Acessórios", 250),
    ("Monitor", "Telas", 900),
    ("Webcam", "Acessórios", 120),
    ("TV", "Telas", 900)
]

print(ordena(produtos))

# feito em 3min13s