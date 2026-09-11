import pytest

from projeto_estacionamento.main import (  # a pasta src nao deve ser referida como diretorio quando vai importar um arquivo
    Caminhao,
    Carro,
    Moto,
    Sistema,
)


# Fixtures podem ser declaradas em cima, e as funcoes que usam a sua saida como parametro podem ficar em qualquer lugar do arquivo
@pytest.fixture
def sistema():
    sistema = Sistema()
    return sistema


@pytest.fixture
def carro():
    carro = Carro("AAC1234")
    return carro


def test_se_entrou(sistema, carro):
    sistema.registra_entrada(carro)
    assert carro.placa in sistema.estacionamento


def test_se_saiu(sistema, carro):
    sistema.registra_entrada(carro)
    sistema.registra_saida(carro, 2.0)
    assert carro.placa not in sistema.estacionamento
    assert carro.__class__.__name__ in sistema.relatorio


def test_tira_falso(sistema, carro):
    sistema.registra_saida(carro, 2.0)
    assert carro.__class__.__name__ not in sistema.relatorio


# O Parametrize precisa estar grudado a funcao que vai usa-lo
@pytest.mark.parametrize(
    "veiculo,tempo,resultado_esperado",
    [
        (Carro("DFS3355"), 0.5, 12),
        (Carro("DFS3355"), 1.0, 12),
        (Carro("DFS3355"), 2.0, 20),
        (Moto("LFG6781"), 0.5, 6),
        (Moto("LFG6781"), 3.5, 18),
        (Caminhao("POP9034"), 0.5, 40),
        (Caminhao("POP9034"), 2.5, 70),
    ],
)
def test_registra(veiculo, tempo, resultado_esperado):
    assert veiculo.registra_saida_e_calcula_tarifa(tempo) == resultado_esperado
