from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Sistema:
    estacionamento: dict = field(default_factory=dict)
    relatorio: dict = field(default_factory=dict)

    def registra_entrada(self, veiculo):
        veiculo.registra_entrada()
        self.estacionamento[veiculo.placa] = veiculo

    def registra_saida(self, veiculo, tempo):
        if veiculo.placa in self.estacionamento:
            tarifa = veiculo.registra_saida_e_calcula_tarifa(tempo)
            self.atualiza_relatorio(veiculo, tarifa, tempo)
            del self.estacionamento[veiculo.placa]
            print(f"Veículo de placa {veiculo.placa} saiu do estacionamento")
            print(f"Total que veículo de placa {veiculo.placa} tem a pagar: {tarifa}")
        else:
            print("Veículo não encontrado no estacionamento!")

    def atualiza_relatorio(self, veiculo, tarifa, tempo):
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

    def gera_relatorio(self):
        print("----------------------------------------------")
        print("Relatório Diário do Estacionamento")
        print(
            f"Faturamento total do dia: {sum(dados['Faturamento'] for dados in self.relatorio.values())}"
        )
        for veiculo, dic in self.relatorio.items():
            print(f"Faturamento de {veiculo}: {dic['Faturamento']}")

        print(
            f"Permanência Média: {sum(dados['Tempo Total'] for dados in self.relatorio.values()) / sum(dados['Quantidade Veiculos'] for dados in self.relatorio.values()) if sum(dados['Quantidade Veiculos'] for dados in self.relatorio.values()) != 0 else 0.0:.2f}"
        )
        print("----------------------------------------------")

    def verifica(self, veiculo):
        if veiculo.placa in self.estacionamento:
            print(f"Veículo de placa {veiculo.placa} está estacionado")
        else:
            print(f"Veículo de placa {veiculo.placa} não está estacionado")


@dataclass
class Veiculo(ABC):
    placa: str
    # horario_entrada: datetime | None = None #field(default_factory=datetime.now) #uso o field para incia-lo com um valor padrao
    # horario_saida: datetime | None = None #uso isso para inicia-lo como vazio
    tempo_estacionado: float = 0.0

    def registra_entrada(self):
        # self.horario_entrada = datetime.now()
        print(f"Veículo de placa {self.placa} estacionado!")

    @abstractmethod
    def registra_saida_e_calcula_tarifa(self, tempo):
        pass


class Carro(Veiculo):
    def registra_saida_e_calcula_tarifa(self, tempo):
        # self.horario_saida = datetime.now()
        # tempo = (self.horario_saida - self.horario_entrada).total_seconds()
        # tempo = tempo/3600
        tarifa = (
            12  # agora, qualquer tempo menor ou igual a 1 hora paga o valor cheio (12)
        )
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
        tarifa = (
            6  # agora, qualquer tempo menor ou igual a 1 hora paga o valor cheio (6)
        )
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
        while tempo > 0:
            tarifa += 15
            tempo -= 1
        return tarifa


class Onibus(Veiculo):
    def registra_saida_e_calcula_tarifa(self, tempo):
        # self.horario_saida = datetime.now()
        # tempo = (self.horario_saida - self.horario_entrada).total_seconds()
        # tempo = tempo/3600
        tarifa = 30
        while tempo > 0:
            tarifa += 20
            tempo -= 1
        return tarifa


@dataclass
class Mensalista(Carro):
    franquia_restante: float = 200.0

    def verifica_franquia(self, tempo):
        # self.horario_saida = datetime.now()
        # tempo = (self.horario_saida - self.horario_entrada).total_seconds()
        # tempo = tempo/3600
        self.franquia_restante -= tempo
        if self.franquia_restante <= 0:
            # aqui, discuti com o Gemini, e poderia usar o super() para chamar a funcao de calcular tarifa da classe pai (Carro())
            pass


if __name__ == "__main__":
    carro1 = Carro("AAC1234")
    print(carro1.__class__)
    print(carro1.__class__.__name__)
    print(type(carro1.__class__.__name__))
    # Teste 1: Veja o tipo de cada elemento
    # print(type(Carro))   # O que retorna?
    # print(type(carro1))  # O que retorna?

    # Teste 2: Tente acessar a tupla de atributos da instância vs classe
    # print(dir(carro1))   # Procure se __name__ está aqui
    # print(dir(Carro))    # Procure se __name__ está aqui
    # print(str(carro1))

    caminhao1 = Caminhao("JJE4545")
    caminhao2 = Caminhao("ABB7265")
    moto1 = Moto("FOF3100")
    onibus1 = Onibus("LFF5439")

    estacionamento_centro = Sistema()
    # print(repr(estacionamento_centro))
    estacionamento_centro.registra_entrada(carro1)
    estacionamento_centro.registra_entrada(caminhao1)
    estacionamento_centro.registra_entrada(caminhao2)
    estacionamento_centro.registra_entrada(moto1)
    estacionamento_centro.registra_entrada(onibus1)
    # print(repr(estacionamento_centro))
    # print(estacionamento_centro.estacionamento)
    estacionamento_centro.verifica(carro1)
    # estacionamento_centro.verifica(moto1)
    estacionamento_centro.registra_saida(carro1, 2.0)
    # estacionamento_centro.gera_relatorio()
    estacionamento_centro.registra_saida(caminhao1, 2.5)
    # estacionamento_centro.registra_saida(caminhao2, 1.5)
    estacionamento_centro.registra_saida(moto1, 4.0)
    estacionamento_centro.registra_saida(onibus1, 2.5)
    estacionamento_centro.gera_relatorio()

    # print(repr(moto1))
    # print(repr(cliente1))
