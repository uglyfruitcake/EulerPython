import my_module
import itertools


permutations = itertools.permutations('1234567', 7)
intpermutations = [int("".join(i)) for i in permutations]
primes = []
for n in intpermutations:
    if my_module.is_prime(n):
        print(n)
        primes.append(n)
print(max(primes))
