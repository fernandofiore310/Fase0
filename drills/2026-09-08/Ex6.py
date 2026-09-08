def acha_temp(temperaturas):
    print(f"Algo acima de 30: {any(t > 30 for t in temperaturas)}")
    print(f"Todos acima de 0: {all(t > 0 for t in temperaturas)}")

temperaturas = [18, 22, 31, 27, 15]
acha_temp(temperaturas)

#feito em 6min