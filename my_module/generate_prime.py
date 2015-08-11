import my_module


def generate_prime(floor, ceiling):
    primes = []
    for i in xrange(floor, ceiling):
        if my_module.is_prime(i):
            primes.append(i)
    return primes
