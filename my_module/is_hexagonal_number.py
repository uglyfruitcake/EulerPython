def is_hexagonal_number(n):
    if ((((8 * n) + 1) ** 0.5) + 1) % 4 == 0:
        return(True)
    return(False)
