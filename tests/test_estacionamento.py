import pytest

from projeto_estacionamento.main import (  # a pasta src nao deve ser referida como diretorio quando vai importar um arquivo
    Caminhao,
    Carro,
    Mensalista,
    Moto,
    Onibus,
    Sistema,
    Veiculo,
)


# Fixtures podem ser declaradas em cima, e as funcoes que usam a sua saida como parametro podem ficar em qualquer lugar do arquivo
@pytest.fixture
def sistema() -> Sistema:
    sistema = Sistema()
    return sistema


@pytest.fixture
def carro() -> Carro:
    carro = Carro("AAC1234")
    return carro


def test_se_entrou(sistema: Sistema, carro: Carro):
    sistema.registra_entrada(carro)
    assert carro.placa in sistema.estacionamento


def test_se_saiu(sistema: Sistema, carro: Carro):
    sistema.registra_entrada(carro)
    sistema.registra_saida(carro, 2.0)
    assert carro.placa not in sistema.estacionamento
    assert carro.__class__.__name__ in sistema.relatorio
    assert sistema.relatorio[carro.__class__.__name__]["Faturamento"] == 20


def test_tira_falso(sistema: Sistema, carro: Carro):
    sistema.registra_saida(carro, 2.0)
    assert carro.__class__.__name__ not in sistema.relatorio


# O Parametrize precisa estar grudado a funcao que vai usa-lo
@pytest.mark.parametrize(
    "veiculo,tempo,resultado_esperado",
    [
        (Carro, 0.5, 12),
        (Carro, 1.0, 12),
        (Carro, 2.0, 20),
        (Moto, 0.5, 6),
        (Moto, 3.5, 18),
        (Caminhao, 0.5, 40),
        (Caminhao, 2.5, 70),
        (Onibus, 2.5, 90),
        (Mensalista, 196.7, 0),
        (Mensalista, 200.0, 0),
        (Mensalista, 202, 20),
    ],
)
def test_registra(veiculo: type[Veiculo], tempo: float, resultado_esperado: float):
    assert (
        veiculo("LFG6565").registra_saida_e_calcula_tarifa(tempo) == resultado_esperado
    )


def test_mensalista():
    mensalista = Mensalista("FFF8888")
    mensalista.registra_saida_e_calcula_tarifa(200.0)
    assert mensalista.franquia_restante == 0


def test_mensalista2():
    mensalista = Mensalista("LFF8888")
    mensalista.registra_saida_e_calcula_tarifa(160.0)
    assert mensalista.franquia_restante == 40


def test_permanencia(sistema: Sistema):
    carro1 = Carro("AAC1234")
    moto1 = Moto("XPT0909")
    bus1 = Onibus("XPL0909")
    mensalista1 = Mensalista("XET0909")

    sistema.registra_entrada(carro1)
    sistema.registra_entrada(moto1)
    sistema.registra_entrada(bus1)
    sistema.registra_entrada(mensalista1)

    sistema.registra_saida(carro1, 2.0)
    sistema.registra_saida(moto1, 1.0)
    sistema.registra_saida(bus1, 0.5)
    sistema.registra_saida(mensalista1, 8.5)

    _, permanencia = sistema.calcula_relatorio()
    assert permanencia == 3.0
