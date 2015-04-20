import my_module

number = 600851475143
primes = my_module.generate_prime(10000)
prime_factors = []

for i in primes:
    if number % i == 0:
        prime_factors.append(i)

print max(prime_factors)
