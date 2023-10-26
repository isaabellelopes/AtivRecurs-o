def pertence_a_W(s):

    if s == "a" or s == "b":
        return True

    if s[0] == 'a' and s[-1] == 'c':
        return pertence_a_W(s[1:-1])

    if s[0] == 'a':
        indice = s.find('c', 1)
        if indice != -1:
            return pertence_a_W(s[1:indice] + s[indice + 1:])

    return False

cadeias = ["a", "ab", "aba", "aaab", "bbbbb"]

for cadeia in cadeias:
    if pertence_a_W(cadeia):
        print(f"'{cadeia}' pertence à coleção W")
    else:
        print(f"'{cadeia}' não pertence à coleção W")