def acha_produto(produtos):
    print(f"Produto mais caro: {max(produtos, key=lambda x : x[1])[0]} - {max(produtos, key=lambda x : x[1])[1]}")

produtos = [
    ("Mouse", 120),
    ("Teclado", 250),
    ("Monitor", 900),
    ("Webcam", 300)
]
acha_produto(produtos=produtos)

# resolvido em 6min