import my_module


consecutives = 0
for i in xrange(1, 1000000):
    if consecutives == 4:
        break
    if len(my_module.get_distinct_prime_factors(i)) == 4:
        consecutives += 1
    else:
        consecutives = 0

print(i - 4)
