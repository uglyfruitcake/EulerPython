import my_module
import itertools


total = 0
pandigitals = itertools.permutations('0123456789', 10)
pandigitals = [int("".join(i)) for i in pandigitals]
primes = [2, 3, 5, 7, 11, 13, 17]
for n in pandigitals:
    digits = [i for i in str(n)]
    for i in xrange(1, 8):
        if int("".join(digits[i:i + 3])) % primes[i - 1] != 0:
            total += n
            break

print(sum(pandigitals) - total)
