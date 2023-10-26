def cadeias_binarias_impares(n):

    if n == 1: 
        return ["0"]
    elif n == 0:
        return []
    else:
        cadeias_pares = cadeias_binarias_impares(n-1)
        cadeias_impares = []
        for cadeia in cadeias_pares:
            cadeias_impares.append("0" + cadeia)
        return cadeias_pares + cadeias_impares