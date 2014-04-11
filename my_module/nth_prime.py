import my_module


def nth_prime(n):
    number = 0
    possible_prime = 1
    while number < n:
        if my_module.is_prime(possible_prime):
            number += 1
        possible_prime += 1
    return possible_prime - 1
