def ordena_produtos(nomes, precos):
    # print(list(zip(nomes, precos)))
    return {nome : preco for nome, preco in zip(nomes, precos) if preco > 100}

nomes = ["Mouse", "Teclado", "Monitor", "Webcam"]
precos = [80, 150, 900, 70]

print(ordena_produtos(nomes, precos))

# feito em 3min55s