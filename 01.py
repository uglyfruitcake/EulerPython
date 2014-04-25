import my_module

sum_of_multiples = 0

for i in xrange(3, 1000):
    if my_module.is_multiple_of_x(i, 3):
        sum_of_multiples += i
    else:
        if my_module.is_multiple_of_x(i, 5):
            sum_of_multiples += i

print sum_of_multiples
