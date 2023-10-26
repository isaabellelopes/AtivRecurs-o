##EXER 8.A

def sequenA(n):
    if n == 1:

        return 1

    else:

        return 3 * sequenA(n - 1)

##EXER 8.B


def sequenB(n):
    if n == 1:

        return 2

    elif n == 2:

        return 1

    elif n % 2 == 0:

        return 2 * sequenB(n - 2)

    else:

        return sequenB(n - 2)

##EXER 8.C


def sequenC(n, a, b):
    if n == 1:

        return a

    elif n == 2:

        return b

    else:

        return sequenC(n - 1, a, b) + (n - 2) * b

##EXER 8.D


def sequenD(n, p, q):
    if n == 1:

        return p

    elif n == 2:

        return p - q

    elif n % 2 == 0:

        return sequenD(n - 1, p, q) + 2 * q

    else:

        return sequenD(n - 1, p, q) - (n // 2) * q