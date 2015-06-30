import my_module


amicable_numbers = []
for i in xrange(1, 10000):
    if my_module.is_amicable_number(i):
        amicable_numbers.append(i)
print sum(amicable_numbers)
