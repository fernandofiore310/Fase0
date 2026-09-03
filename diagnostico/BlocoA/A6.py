def conta_error(log):
    log = log.split()

    tamanho = 0
    for c in log:
        tamanho += 1
    
    i = 0
    quantidade_errors = 0
    while i < tamanho:
        if i % 3 == 0 and log[i] == "ERROR":
            quantidade_errors += 1
    return quantidade_errors


conta_error("Oi tudo bem?")