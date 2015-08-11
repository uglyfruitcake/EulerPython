import my_module


sum_of_primes = 0

for i in my_module.generate_prime(2, 2000000):
    sum_of_primes += i

print sum_of_primes
