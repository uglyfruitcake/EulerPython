import my_module


def get_proper_divisors(n):
    divisors = [1]
    for i in xrange(2, n):
        if my_module.is_factor(i, n):
            divisors.append(i)
    return divisors
