import my_module


def consecutive_primes_from_quadratic(a, b):
    primes = 0
    for i in xrange(0, 100000):
        if ((i ** 2) + (i * a) + b) > 1:
            if my_module.is_prime((i ** 2) + (i * a) + b):
                primes += 1
            else:
                break
    return(primes)
