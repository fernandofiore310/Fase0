from collections import Counter


def conta_votos(votos):
    contagem = dict(Counter(votos))
    # print(contagem)
    candidato, votos = max(contagem, key=lambda x : contagem.values())
    # nao seu tempo de acabar, mas o correto seria candidato = max(contagem, key=lambda x : contagem[x])
    # candidato = max(contagem, key=lambda x : contagem[x])

    print(f"Mais votado: {candidato}")

votos = ["A", "B", "A", "C", "B", "A"]
conta_votos(votos)

# estourei os 6 min