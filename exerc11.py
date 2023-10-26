lista = [3, 7, 4, 2, 6]


def rotina(lista, intJ):
    if intJ == 1:
        return lista

    maior = 0

    for i in range(0, intJ):
        if lista[i] > maior:
            maior = lista[i]
        print(f"Chamadas: {i}")

    index = lista.index(maior)
    lista[index] = lista[len(lista) - 1]
    lista[len(lista) - 1] = maior
    print(lista)

rotina(lista, 5)
