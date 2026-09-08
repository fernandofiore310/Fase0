def aplica_desconto(dic):
    return {produto : preco-preco*0.1 for produto, preco in dic.items() if preco >= 100}

produtos = {
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 900,
    "Webcam": 70
}

print(aplica_desconto(produtos))

# feito em 2min54s