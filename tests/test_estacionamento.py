import pytest

from projeto_estacionamento.main import (  #a pasta src nao deve ser referida como diretorio quando vai importar um arquivo
    Caminhao,
    Carro,
    Moto,
)


#Fixtures podem ser declaradas em cima, e as funcoes que usam a sua saida como parametro podem ficar em qualquer lugar do arquivo
@pytest.fixture
def caminhao():
    caminhao = Caminhao("JJE4545")
    return caminhao

@pytest.fixture
def carro():
    carro = Carro("AAC1234")
    return carro

def test_calcular_tarifa_correta_caminhao(caminhao):
    tarifa = caminhao.registra_saida_e_calcula_tarifa(2.5)
    assert tarifa == 55

def test_calcular_tarifa_errada_caminhao(caminhao):
    tarifa = caminhao.registra_saida_e_calcula_tarifa(2.5)
    assert tarifa != 60

def test_calcular_tarifa_correta(carro):
    tarifa = carro.registra_saida_e_calcula_tarifa(2.5)
    assert tarifa == 28

def test_calcular_tarifa_errada(carro):
    tarifa = carro.registra_saida_e_calcula_tarifa(2.5)
    assert tarifa != 30

# O Parametrize precisa estar grudado a funcao que vai usa-lo
@pytest.mark.parametrize(
    "tempo,resultado_esperado",
    [
        (2.5, 28),
        (2, 20),
        (3, 28),
        (3.5, 36),
    ]
)
def test_registra(carro, tempo, resultado_esperado):
    assert carro.registra_saida_e_calcula_tarifa(tempo) == resultado_esperado

# Fiz os testes de moto sem o fixture apenas pela experiencia
def test_calcular_tarifa_correta_moto():
    moto = Moto("FOF3100")
    tarifa = moto.registra_saida_e_calcula_tarifa(2.5)
    assert tarifa == 14

def test_calcular_tarifa_errada_moto():
    moto = Moto("FOF3100")
    tarifa = moto.registra_saida_e_calcula_tarifa(2.5)
    assert tarifa != 20