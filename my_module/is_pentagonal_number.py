def is_pentagonal_number(n):
    n = ((24 * n + 1) ** 0.5) % 6
    if n == 5:
        return(True)
    return(False)
