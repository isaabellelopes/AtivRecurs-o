def progressao_geometrica(n, a, r): 
    if n == 1:
        return a
    else:
        return r * progressao_geometrica(n-1, a, r)