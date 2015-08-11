import my_module
import itertools

allprimes = []
primes = my_module.generate_prime(1000, 10001)
for n in primes:
    permutations = set([int("".join(i)) for i in itertools.permutations(str(n), 4)])
    primepermutations = []
    for i in permutations:
        if i in primes:
            primepermutations.append(i)
    if len(primepermutations) > 2:
        primepermutations = sorted(primepermutations, key=int)
        if primepermutations not in allprimes:
            allprimes.append(primepermutations)

for n in allprimes:
    for a in n:
        for b in n:
            for c in n:
                if a > b > c:
                    if a - b == b - c:
                        if a != 8147:
                            print("".join([str(c), str(b), str(a)]))
