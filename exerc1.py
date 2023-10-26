EXERCICIO 1

# EXER 1.A

def ex1A(n):
    if n == 1:

        return 10

    else:

        return ex1A(n - 1) + 10

# EXER 1.B


def ex1B(n):
    if n == 1:

        return 2

    else:

        return ex1B(n - 1) - 1

# EXER 1.C


def ex1C(n):
    if n == 1:

        return 1

    else:

        return ex1C(n - 1) + n ** 2

# EXER 1.D


def ex1D(n):
    if n == 1:

        return 1

    else:

        return n ** 2 * ex1D(n - 1) + n - 1

# EXER 1.E


def ex1E(n):
    if n == 1:

        return 3

    elif n == 2:

        return 5

    else:

        return (n - 1) * ex1E(n - 1) + (n - 2) * ex1E(n - 2)

# EXER 1.F


def ex1F(n):
    if n == 1:

        return 2

    elif n == 2:

        return 5

    else:

        return ex1F(n - 1) * ex1F(n - 2)

# EXER 1.G


def ex1G(n):
    if n == 1:

        return 1

    elif n == 2:

        return 2

    elif n == 3:

        return 3
    else:

        return ex1G(n - 1) + 2 * ex1G(n - 2) + 3 * ex1G(n - 3)