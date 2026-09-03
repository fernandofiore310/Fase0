import time

class Sistema:

    def __init__(self):
        self.veiculos = []
        self.relatorio = {"faturamento_total" : 0,
                          "faturamento_por_veiculo" : {"Carro": 0, "Moto": 0, "Caminhao": 0},
                          "permanencia_media" : 0,
                          }

    def registra_entrada(cliente):
        cliente.entrada = time.time() #esta em segundos
        Sistema.veiculos.append(cliente)

    def registra_saida(cliente):
        cliente.saida = time.time()
    
        tempo = cliente.saida - cliente.entrada
        tempo = tempo/3600

        if cliente.mensalista == True:
            cliente.tempo_mensalista += tempo
            if cliente.tempo_mensalista > 200:
                tempo_extra = cliente.tempo_mensalista - 200
                if tempo_extra < 1:
                    cliente.preco_a_pagar += 8
                else:
                    cliente.preco_a_pagar += 12
                    tempo_extra -= 1
                    while tempo_extra >= 0:
                        cliente.preco_a_pagar += 8
                        tempo_extra -= 1
            Sistema.relatorio["faturamento_por_veiculo"]["Carro"] += cliente.preco_a_pagar
        else:
            if cliente.veiculo == "Carro":
                if tempo < 1:
                    cliente.preco_a_pagar += 8
                else:
                    cliente.preco_a_pagar += 12
                    tempo -= 1
                    while tempo >= 0:
                        cliente.preco_a_pagar += 8
                        tempo -= 1
                Sistema.relatorio["faturamento_por_veiculo"]["Carro"] += cliente.preco_a_pagar

            elif cliente.veiculo == "Moto":
                if tempo < 1:
                    cliente.preco_a_pagar += 4
                else:
                    cliente.preco_a_pagar += 6
                    tempo -= 1
                    while tempo >= 0:
                        cliente.preco_a_pagar += 4
                        tempo -= 1
                Sistema.relatorio["faturamento_por_veiculo"]["Moto"] += cliente.preco_a_pagar

            elif cliente.veiculo == "Caminhao":
                cliente.preco_a_pagar += 25
                while tempo >= 0:
                    cliente.preco_a_pagar += 15
                    tempo -= 1
                Sistema.relatorio["faturamento_por_veiculo"]["Caminhao"] += cliente.preco_a_pagar

            else:
                return "Veiculo nao identificado"

        Sistema.relatorio["faturamento_total"] += cliente.preco_a_pagar

        Sistema.veiculos.remove(cliente)

    def gera_relatorio():
        teste = 1 #teste do pull request

class Cliente:

    def __init__(self, mensalista, veiculo):
        self.mensalista = mensalista
        self.veiculo = veiculo
        self.entrada = None
        self.saida = None
        self.tempo_mensalista = None
        self.preco_a_pagar = 0


# t1 = time.time()
# time.sleep(4)
# t2 = time.time()
# print(t2 - t1)