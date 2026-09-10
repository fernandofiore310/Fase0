from datetime import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Sistema:
    estacionamento : dict = field(default_factory=dict)
    relatorio : dict = field(default_factory=dict)

    def registra_entrada(self, veiculo):
        veiculo.registra_entrada()
        self.estacionamento[veiculo.placa] = [veiculo, 0]

    def registra_saida(self, veiculo, tempo):
        tarifa = veiculo.registra_saida_e_calcula_tarifa(tempo)
        print(f"Total a pagar: {tarifa}")
        self.atualiza_relatorio(veiculo, tarifa)

    def atualiza_relatorio(self, veiculo, tarifa):
        pass

    def verifica(self, veiculo):
        for placa in self.estacionamento:
            if veiculo.placa == placa:
                return "Veículo estacionado"
        return "Veículo não estacionado"

@dataclass
class Veiculo(ABC):
    placa : str
    # horario_entrada: datetime | None = None #field(default_factory=datetime.now) #uso o field para incia-lo com um valor padrao
    # horario_saida: datetime | None = None #uso isso para inicia-lo como vazio
    tempo_estacionado: float = 0.0

    def registra_entrada(self):
        self.horario_entrada = datetime.now()

    @abstractmethod
    def registra_saida_e_calcula_tarifa(self, tempo):
        pass

class Carro(Veiculo):

    def registra_saida_e_calcula_tarifa(self, tempo):
        # self.horario_saida = datetime.now()
        # tempo = (self.horario_saida - self.horario_entrada).total_seconds()
        # tempo = tempo/3600
        tarifa = 0
        if tempo < 1:
            tarifa += 12
        else:
            tarifa += 12
            tempo -= 1
            while tempo > 0:
                tarifa += 8
                tempo -= 1
        return tarifa

class Moto(Veiculo):

    def registra_saida_e_calcula_tarifa(self, tempo):
        # self.horario_saida = datetime.now()
        # tempo = (self.horario_saida - self.horario_entrada).total_seconds()
        # tempo = tempo/3600
        tarifa = 0
        if tempo < 1:
            tarifa += 6
        else:
            tarifa += 6
            tempo -= 1
            while tempo > 0:
                tarifa += 4
                tempo -= 1
        return tarifa

class Caminhao(Veiculo):

    def registra_saida_e_calcula_tarifa(self, tempo):
        # self.horario_saida = datetime.now()
        # tempo = (self.horario_saida - self.horario_entrada).total_seconds()
        # tempo = tempo/3600
        tarifa = 25
        tempo -= 1
        while tempo > 0:
            tarifa += 15
            tempo -= 1
        return tarifa


if __name__ == "__main__":

    carro1 = Carro("AAC1234")
    caminhao1 = Caminhao("JJE4545")
    moto1 = Moto("FOF3100")

    estacionamento_centro = Sistema()
    print(repr(estacionamento_centro))
    estacionamento_centro.registra_entrada(carro1)
    print(repr(estacionamento_centro))
    print(estacionamento_centro.verifica(carro1))
    print(estacionamento_centro.verifica(moto1))
    estacionamento_centro.registra_saida(carro1, 2.0)

    # print(repr(moto1))
    # print(repr(cliente1))
