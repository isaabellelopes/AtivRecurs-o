M = [6, 9, 16, 21, 26, 54, 72, 218]

def collectionM(n):
    if n == 2 or n == 3:
        return True

    for i in range(2, n // 2 + 1):
        if n % i == 0 and collectionM(i) and collectionM(n // i):
            return True

    return False


for n in M:
    if collectionM(n):
        print(f"{n} pertence à coleção M")
    else:
        print(f"{n} não pertence à coleção M")
