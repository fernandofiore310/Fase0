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


log = """2026-09-03 08:12:07 ERROR Aplicação iniciada com sucesso
2026-09-03 08:14:31 INFO Conexão com o banco de dados estabelecida
2026-09-03 08:27:45 WARNING Tempo de resposta acima do esperado
2026-09-03 09:03:18 INFO Usuário autenticado com sucesso
2026-09-03 09:41:52 ERROR Falha ao carregar arquivo de configuração
2026-09-03 09:42:10 INFO Tentando carregar configuração padrão
2026-09-03 10:15:01 INFO Configuração padrão carregada com sucesso
2026-09-03 10:48:33 WARNING Uso de memória acima de 75 por cento
2026-09-03 11:22:10 INFO Requisição recebida no endpoint de usuários
2026-09-03 11:22:11 ERROR Erro ao processar dados da requisição
2026-09-03 11:57:19 INFO Requisição encerrada com status 500
2026-09-03 12:34:04 INFO Nova tentativa de conexão com serviço externo
2026-09-03 12:48:09 WARNING Serviço externo respondeu com atraso
2026-09-03 13:05:12 INFO Resposta do serviço externo recebida
2026-09-03 13:46:45 INFO Cache atualizado com sucesso
2026-09-03 14:30:02 ERROR Não foi possível salvar registro no banco de dados
2026-09-03 14:44:18 WARNING Tentativa de escrita será repetida
2026-09-03 15:02:25 INFO Registro salvo com sucesso na segunda tentativa
2026-09-03 15:39:37 INFO Processo de sincronização iniciado
2026-09-03 16:18:06 WARNING Foram encontrados registros duplicados
2026-09-03 16:52:44 INFO Registros duplicados foram ignorados
2026-09-03 17:33:21 ERROR Falha de conexão com o servidor de autenticação
2026-09-03 18:04:40 INFO Reconectando ao servidor de autenticação
2026-09-03 18:17:46 INFO Conexão restabelecida com sucesso
2026-09-03 19:26:10 INFO Aplicação operando normalmente"""

print(conta_error(log))