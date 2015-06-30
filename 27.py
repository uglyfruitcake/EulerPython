import my_module


maxprimes = 0
product = 0
for a in xrange(-1000, 1001):
    for b in xrange(-1000, 1001):
        if my_module.consecutive_primes_from_quadratic(a, b) > maxprimes:
            maxprimes = my_module.consecutive_primes_from_quadratic(a, b)
            product = a * b
print(product)
