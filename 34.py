import my_module


factorials = 0
for i in xrange(145, 100000):
    factorial_of_digits = 0
    for d in my_module.array_of_digits(i):
        total = 1
        for n in xrange(1, d + 1):
            total *= n
        factorial_of_digits += total
    if factorial_of_digits == i:
        print(i)
        factorials += i

print(factorials)
