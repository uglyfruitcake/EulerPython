import my_module


sumofprimes = 0
for i in xrange(10, 1000000):
    if my_module.is_truncatable_prime(i):
        sumofprimes += i
print(sumofprimes)
