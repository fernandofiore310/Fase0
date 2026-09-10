from main import Sistema, Veiculo, Carro, Caminhao, Moto
import pytest

@pytest.fixture
def sistema():
    sistema = Sistema()
    return sistema

@pytest.mark.parametrize(
    "tempo,resultado_esperado",
    [
        (2.5, 28),
        (2, 20),
        (3, 28),
        (3.5, 36),
    ]
)

@pytest.fixture
def carro():
    carro = Carro("AAC1234")
    return carro

def test_calcular_tarifa_correta(carro):
    tarifa = carro.registra_saida_e_calcula_tarifa(2.5)
    assert tarifa == 28

def test_calcular_tarifa_errada(carro):
    tarifa = carro.registra_saida_e_calcula_tarifa(2.5)
    assert tarifa == 30

def test_registra(carro, tempo, resultado_esperado):
    assert carro.registra_saida_e_calcula_tarifa(tempo) == resultado_esperado
