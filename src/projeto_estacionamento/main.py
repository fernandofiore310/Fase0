from abc import ABC, abstractmethod
from dataclasses import dataclass, field


def calcula_tarifa_carro(tempo: float) -> float:
    tarifa = 12  # agora, qualquer tempo menor ou igual a 1 hora paga o valor cheio (12)
    tempo -= 1
    while tempo > 0:
        tarifa += 8
        tempo -= 1
    return tarifa


@dataclass
class Veiculo(ABC):
    placa: str

    def registra_entrada(self):
        print(f"Veículo de placa {self.placa} estacionado!")

    @abstractmethod
    def registra_saida_e_calcula_tarifa(self, tempo: float) -> float:
        pass


class Carro(Veiculo):
    def registra_saida_e_calcula_tarifa(self, tempo: float) -> float:
        return calcula_tarifa_carro(tempo=tempo)


class Moto(Veiculo):
    def registra_saida_e_calcula_tarifa(self, tempo: float) -> float:
        tarifa = (
            6  # agora, qualquer tempo menor ou igual a 1 hora paga o valor cheio (6)
        )
        tempo -= 1
        while tempo > 0:
            tarifa += 4
            tempo -= 1
        return tarifa


class Caminhao(Veiculo):
    def registra_saida_e_calcula_tarifa(self, tempo: float) -> float:
        tarifa = 25
        while tempo > 0:
            tarifa += 15
            tempo -= 1
        return tarifa


class Onibus(Veiculo):
    def registra_saida_e_calcula_tarifa(self, tempo: float) -> float:
        tarifa = 30
        while tempo > 0:
            tarifa += 20
            tempo -= 1
        return tarifa


@dataclass
class Mensalista(Veiculo):
    franquia_restante: float = 200.0

    def registra_saida_e_calcula_tarifa(self, tempo: float) -> float:
        tarifa = 0.0
        if self.franquia_restante - tempo > 0:
            self.franquia_restante -= tempo
        else:
            tempo = -(self.franquia_restante - tempo)
            if tempo == 0:
                tarifa = 0
            else:
                tarifa = calcula_tarifa_carro(tempo=tempo)
            self.franquia_restante = 0
        return tarifa


@dataclass
class Sistema:
    estacionamento: dict = field(default_factory=dict)
    relatorio: dict = field(default_factory=dict)

    def registra_entrada(self, veiculo: Veiculo):
        veiculo.registra_entrada()
        self.estacionamento[veiculo.placa] = veiculo

    def registra_saida(self, veiculo: Veiculo, tempo: float):
        if veiculo.placa in self.estacionamento:
            tarifa = veiculo.registra_saida_e_calcula_tarifa(tempo)
            self.atualiza_relatorio(veiculo, tarifa, tempo)
            del self.estacionamento[veiculo.placa]
            print(f"Veículo de placa {veiculo.placa} saiu do estacionamento")
            print(f"Total que veículo de placa {veiculo.placa} tem a pagar: {tarifa}")
        else:
            print("Veículo não encontrado no estacionamento!")

    def atualiza_relatorio(self, veiculo: Veiculo, tarifa: float, tempo: float):
        nome = veiculo.__class__.__name__
        if nome not in self.relatorio:
            self.relatorio[nome] = {}
            self.relatorio[nome]["Faturamento"] = tarifa
            self.relatorio[nome]["Quantidade Veiculos"] = 1
            self.relatorio[nome]["Tempo Total"] = tempo
        else:
            self.relatorio[nome]["Faturamento"] += tarifa
            self.relatorio[nome]["Quantidade Veiculos"] += 1
            self.relatorio[nome]["Tempo Total"] += tempo

    def calcula_relatorio(self) -> tuple[float, float]:
        faturamento_total = sum(
            dados["Faturamento"] for dados in self.relatorio.values()
        )
        tempo_total = sum(dados["Tempo Total"] for dados in self.relatorio.values())
        quantidade_veiculos = sum(
            dados["Quantidade Veiculos"] for dados in self.relatorio.values()
        )

        if quantidade_veiculos != 0:
            permanencia_media = tempo_total / quantidade_veiculos
        else:
            permanencia_media = 0.0
        return faturamento_total, permanencia_media

    def gera_relatorio(self):
        f, p = self.calcula_relatorio()
        print("----------------------------------------------")
        print("Relatório Diário do Estacionamento")
        print(f"Faturamento total do dia: {f}")
        for veiculo, dic in self.relatorio.items():
            print(f"Faturamento de {veiculo}: {dic['Faturamento']}")

        print(f"Permanência Média: {p:.2f}")
        print("----------------------------------------------")

    def verifica(self, veiculo):
        if veiculo.placa in self.estacionamento:
            print(f"Veículo de placa {veiculo.placa} está estacionado")
        else:
            print(f"Veículo de placa {veiculo.placa} não está estacionado")


if __name__ == "__main__":
    carro1 = Carro("AAC1234")
    caminhao1 = Caminhao("JJE4545")
    caminhao2 = Caminhao("ABB7265")
    moto1 = Moto("FOF3100")
    moto2 = Moto("FPF3100")
    onibus1 = Onibus("LFF5439")
    mensalista1 = Mensalista("LFF5434")

    estacionamento_centro = Sistema()
    estacionamento_centro.registra_entrada(carro1)
    estacionamento_centro.registra_entrada(caminhao1)
    estacionamento_centro.registra_entrada(caminhao2)
    estacionamento_centro.registra_entrada(moto1)
    estacionamento_centro.registra_entrada(onibus1)
    estacionamento_centro.registra_entrada(mensalista1)

    estacionamento_centro.verifica(carro1)
    estacionamento_centro.verifica(moto2)

    estacionamento_centro.registra_saida(mensalista1, 70.0)
    estacionamento_centro.registra_saida(carro1, 3.0)
    estacionamento_centro.registra_saida(caminhao1, 2.5)
    estacionamento_centro.registra_saida(caminhao2, 1.5)
    estacionamento_centro.registra_saida(moto1, 4.0)
    estacionamento_centro.registra_saida(onibus1, 2.5)

    estacionamento_centro.gera_relatorio()
