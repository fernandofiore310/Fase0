def acha_aluno(alunos):
    nome, nota = min(alunos, key=lambda x : x[1])
    print(f"Menor nota: {nome} - {nota}")

alunos = [
    ("Ana", 8.5),
    ("Bruno", 6.0),
    ("Carla", 9.2),
    ("Diego", 7.1)
]

acha_aluno(alunos)

#feito em 3min27s