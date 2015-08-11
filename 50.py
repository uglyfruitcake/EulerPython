import my_module


primesums = []
primesumslen = []
primes = my_module.generate_prime(2, 10000)
for a in xrange(1, len(primes)):
    for b in xrange(1, len(primes)):
        if sum(primes[a:][:-b]) < 1000000:
            if my_module.is_prime(sum(primes[a:][:-b])):
                primesums.append(sum(primes[a:][:-b]))
                primesumslen.append(len(primes[a:][:-b]))
print(primesums[primesumslen.index(max(primesumslen))])
