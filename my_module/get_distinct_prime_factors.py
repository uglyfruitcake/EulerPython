import my_module


def get_distinct_prime_factors(n):
    prime_factors = []
    divisors = my_module.get_proper_divisors(n)
    for i in divisors:
        if my_module.is_prime(i):
            prime_factors.append(i)
    return(prime_factors)
