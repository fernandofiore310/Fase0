from dataclasses import dataclass
import datetime

@dataclass
class Sistema:
    def __init__(self):
        self.estacionados = {}

    def __repr__(self):
        return f"Sistema(estacionados={self.estacionados!r})"

    def registra_entrada(self, cliente):
        if cliente.veiculo.placa not in self.estacionados.values():
            cliente.horario_entrada = datetime.now()
            self.estacionados[cliente.veiculo.tipo] = cliente.veiculo.placa
            print(f"Estacionamento confirmado para veículo de placa: {cliente.veiculo.placa}")
        else:
            print(f"Cliente já estacionado! Placa: {cliente.veiculo.placa}")

    def registra_saida(self, cliente):
        if cliente.veiculo.placa not in self.estacionados.values():
            print(f"Veículo de placa {cliente.veiculo.placa} não registrado!")
        else:
            cliente.horario_saida = datetime.now()
            tempo = cliente.horario_saida - cliente.horario_entrada
            del self.estacionados[cliente.veiculo.tipo]

            if cliente.mensalista:
                pass
            else:
                if cliente.veiculo.tipo == "Carro":
                    # Calcula o preco cobrado baseado no tempo
                    pass
                elif cliente.veiculo.tipo == "Caminhao":
                    # Calcula o preco cobrado baseado no tempo
                    pass
                elif cliente.veiculo.tipo == "Moto":
                    # Calcula o preco cobrado baseado no tempo
                    pass
                else:
                    # Calcula o preco cobrado baseado no tempo
                    pass
                    
@dataclass
class Veiculo:
    tipo : str
    placa : str

@dataclass
class Cliente:
    mensalista : bool
    veiculo : Veiculo
    horario_entrada: datetime | None = None
    horario_saida: datetime | None = None

carro1 = Veiculo("Carro", "ABC1234")
caminhao1 = Veiculo("Caminhao", "JJE4545")
moto1 = Veiculo("Moto", "FOF3100")

cliente1 = Cliente(False, carro1)

estacionamento_centro = Sistema()
print(repr(estacionamento_centro))
estacionamento_centro.registra_entrada(cliente1)
estacionamento_centro.registra_entrada(cliente1)
print(repr(estacionamento_centro))

# print(repr(moto1))
# print(repr(cliente1))