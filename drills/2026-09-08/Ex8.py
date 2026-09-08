def organiza(nomes, notas):
    for nome, nota in zip(nomes, notas):
        print(f"{nome} - {nota}")

nomes = ["Ana", "Bruno", "Carlos"]
notas = [9.0, 7.5, 8.2]

organiza(nomes, notas)

#feito em 3min8s