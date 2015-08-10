import my_module


for i in xrange(2, 5800):
    if i % 2 == 1:
        if not my_module.is_prime(i):
            if not my_module.is_goldback_composite(i):
                print(i)
