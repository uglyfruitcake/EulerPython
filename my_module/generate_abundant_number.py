import my_module


def generate_abundant_number(ceiling):
    abundant_numbers = []
    for i in xrange(12, ceiling + 1):
        divisors = my_module.get_proper_divisors
        if sum(my_module.get_proper_divisors(i))>i:
            abundant_numbers.append(i)
    return(abundant_numbers)
