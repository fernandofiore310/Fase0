def produz_numeros(limite):
    seq = [1]
    atual = 1
    i = 0

    while True:
        if i == 0:
            atual = atual + seq[i]
            if atual >= limite:
                break
            seq.append(atual)
        else:
            atual = seq[i] + seq[i-1]
            if atual >= limite:
                break
            seq.append(atual)
        i+=1

    # print(seq)
    soma = 0
    for n in seq:
        soma += n
    return soma

print(produz_numeros(10))


