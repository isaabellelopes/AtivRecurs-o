def con_bacterias(n):
    if n == 0:
        return 50000

    return con_bacterias(n - 1) * 3


n = 0

populacao = 50000

while populacao <= 200000:
    n += 1
    populacao = con_bacterias(n)
print(f"Em {n} leituras a polulação irá exercer 200.000 bactérias")