import my_module


def sum_of_factorial_digits(n):
    total = 1
    for i in xrange(1, n + 1):
        total *= i
    digits = my_module.array_of_digits(total)

    return sum(digits)
