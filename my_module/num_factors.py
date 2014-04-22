import my_module
import math


def num_factors(number):
    possible_factor = 2
    number_factors = 2
    st = math.sqrt(number)

    while possible_factor < st:
        if my_module.is_factor(possible_factor, number):
            number_factors += 2
        possible_factor += 1

    if possible_factor == st:
        number_factors += 1

    if number == 1:
        return 1
    else:
        return number_factors
