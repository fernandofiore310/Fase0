def verifica(usuarios):
    print(f"Todos válidos: {all(idade >= 18 and status for _, idade, status in usuarios)}")

usuarios = [
    ("Ana", 22, True),
    ("Bruno", 19, True),
    ("Carla", 31, True)
]
verifica(usuarios)

#feito em 3min58s