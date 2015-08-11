import my_module
import math


def is_goldback_composite(i):
    primes = my_module.generate_prime(2, i)
    squares = []
    for n in range(1, int(math.ceil(math.sqrt(i)))+1):
        squares.append(2 * (n ** 2))
    for prime in primes:
        for square in squares:
            if prime + square == i:
                return(True)
    return(False)
