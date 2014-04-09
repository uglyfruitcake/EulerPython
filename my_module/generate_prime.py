import my_module


def generate_primes(ceiling):
    primes = []
    for i in xrange(2, ceiling):
        if my_module.is_prime(i):
            primes.append(i)
    return primes
