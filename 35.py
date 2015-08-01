import my_module


count = 0
for i in xrange(1, 1000001):
    if my_module.is_circular_prime(i):
        count += 1
print(count)
