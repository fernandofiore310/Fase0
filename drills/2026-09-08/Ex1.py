def conta_notas(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma/quantidade

    print(f"Quantidade: {quantidade}")
    print(f"Soma: {soma}")
    print(f"Média: {media}")

notas = [6.0, 7.0, 8.0]
conta_notas(notas=notas)

# ex feito em 3min30s