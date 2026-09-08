def conta_error(log):
    dic = {}

    linhas = log.split('\n')
    # print(linhas)
    for linha in linhas:
        linha = linha.split()
        # print(linha)
        if linha[2] == "ERROR":
            hora = linha[1].split(":")[0]
            if hora not in dic:
                dic[hora] = 1
            else:
                dic[hora] += 1
    return dic

with open("logsim.txt", mode='r', encoding="utf-8") as file:
    log = file.read() # Le todo o conteudo do arquivo e o retorna uma string no modo texto 'r' ou como uma sequencia de bytes 'rb'
    # log = file.readlines() Lê todas as linhas e retorna uma lista de strings.
    # log = file.readline() Lê uma única linha por vez, avançando o ponteiro do arquivo.
    # for linha in file: sempre que precisa processar um arquivo texto sequencialmente garantindo eficiência de memória, especialmente quando o arquivo é grande demais para caber confortavelmente na RAM ou quando seu tamanho é desconhecido.
    print(conta_error(log))