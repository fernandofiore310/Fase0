def calcula_vendas(vendas):
    print(f"Total vendido: {sum([valor for _, valor in vendas])}")
    nome, valor = max(vendas, key=lambda x : x[1])
    print(f"Maior venda: {nome} - {valor}")

vendas = [
    ("Ana", 120),
    ("Bruno", 300),
    ("Carla", 180),
    ("Diego", 250)
]

calcula_vendas(vendas)

#feito em 4min42