import math


def is_prime(n):
    if n == 2:
        return True
    elif n == 4:
        return False
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            return False
    return True
